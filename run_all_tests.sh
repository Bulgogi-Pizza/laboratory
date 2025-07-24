#!/bin/bash

#################################
# 사용자 설정 (USER CONFIGURATION)
#################################
# wrk 테스트 설정
TEST_DURATION="10s"
THREADS=4

# 테스트할 서버 정보 (이름:포트)
SERVERS_TO_TEST=(
    "FastAPI:8000"
    "Express:8001"
    "Django:8002"
    "Spring:8080"
)

# 결과 파일 이름
REPORT_FILE="performance_summary_report.md"
MONITOR_LOG="monitor_log.txt"

#################################
# 스크립트 실행 로직 (아래는 수정 불필요)
#################################

# 테스트 실행 함수
run_test() {
    local test_label=$1
    local port=$2
    local path=$3
    local connections=$4
    local url="http://127.0.0.1:$port$path"

    echo "------------------------------------------------------"
    echo ">> 테스트 실행: $test_label"

    # [수정] 포트를 사용하는 모든 프로세스(마스터+자식)의 PID 찾기
    local master_pids=$(lsof -ti :$port)
    if [ -z "$master_pids" ]; then
        echo "!! 경고: 포트 $port 에서 실행 중인 서버를 찾을 수 없습니다. 이 테스트를 건너뜁니다."
        local result_row="| $test_label | N/A (서버 없음) | N/A | N/A | N/A |"
        echo "$result_row" >> $REPORT_FILE
        return
    fi

    # 자식 프로세스까지 모두 포함
    local all_pids_to_monitor=""
    for pid in $master_pids; do
        child_pids=$(pgrep -P $pid)
        all_pids_to_monitor="$all_pids_to_monitor $pid $child_pids"
    done

    # PID 목록에서 중복 제거 및 공백 정리
    all_pids_to_monitor=$(echo $all_pids_to_monitor | tr ' ' '\n' | sort -u | tr '\n' ' ')

    echo "   - 대상 서버: $test_label (Monitoring PIDs: $all_pids_to_monitor) @ $url"

    # [수정] 모든 OS에서 'ps'를 사용하고, 자원 사용량을 합산하는 로직으로 변경
    while true; do
        # ps 결과에서 헤더를 제외하고, 각 프로세스의 CPU와 메모리 사용량 합산
        ps -o %cpu,rss -p "$all_pids_to_monitor" | tail -n +2 | awk '{cpu+=$1; mem+=$2} END {print cpu, mem}'
        sleep 1
    done > $MONITOR_LOG &
    local monitor_pid=$!

    # wrk 실행
    local wrk_output=$(wrk -t$THREADS -c$connections -d$TEST_DURATION $url)

    # 모니터링 종료
    kill $monitor_pid
    wait $monitor_pid 2>/dev/null

    # 결과 분석
    local tps=$(echo "$wrk_output" | grep 'Requests/sec:' | awk '{print $2}')
    local avg_latency=$(echo "$wrk_output" | grep 'Latency' | awk '{print $2}')
    if [ -z "$avg_latency" ]; then
        avg_latency="N/A (에러)"
    fi

    # [수정] 합산된 로그를 바탕으로 평균 계산
    local stats=$(cat $MONITOR_LOG)
    local avg_cpu=$(echo "$stats" | awk '{sum+=$1} END {if (NR > 0) printf "%.2f", sum/NR; else print "0.00"}')
    local avg_mem_kb=$(echo "$stats" | awk '{sum+=$2} END {if (NR > 0) printf "%.0f", sum/NR; else print "0"}')

    local result_row="| $test_label | $tps | $avg_latency | $avg_cpu | $avg_mem_kb |"
    echo "$result_row" >> $REPORT_FILE

    echo "   - 완료. Latency: $avg_latency, TPS: $tps, Total CPU: $avg_cpu%, Total Memory: ${avg_mem_kb}KB"
}

# -------- 메인 실행 블록 --------
echo "# 종합 성능 테스트 결과 (멀티프로세스 자원 합산)" > $REPORT_FILE
echo "" >> $REPORT_FILE
echo "| 테스트 시나리오 | TPS (요청/초) | 평균 Latency | 총 CPU 사용량 (%) | 총 메모리 사용량 (KB) |" >> $REPORT_FILE
echo "|---|---|---|---|---|" >> $REPORT_FILE

for server_info in "${SERVERS_TO_TEST[@]}"; do
    IFS=':' read -r server_name port <<< "$server_info"
    run_test "$server_name - HelloWorld" "$port" "/" "100"
    run_test "$server_name - Fibonacci(25)" "$port" "/calculate/25" "20"
done

rm $MONITOR_LOG
echo ""
echo "======================================================"
echo "✅ 모든 테스트 완료! 종합 결과가 $REPORT_FILE 파일에 저장되었습니다."
echo "======================================================"
echo ""
cat $REPORT_FILE