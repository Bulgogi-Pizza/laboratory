# 종합 성능 테스트 결과 (멀티프로세스 자원 합산)

| 테스트 시나리오 | TPS (요청/초) | 평균 Latency | 총 CPU 사용량 (%) | 총 메모리 사용량 (KB) |
|---|---|---|---|---|
| FastAPI - HelloWorld | 23201.41 | 7.01ms | 612.26 | 299878 |
| FastAPI - Fibonacci(25) | 606.72 | 36.32ms | 957.87 | 288525 |
| Express - HelloWorld | 97786.11 | 2.70ms | 703.98 | 926138 |
| Express - Fibonacci(25) | 14306.10 | 1.70ms | 1004.47 | 963034 |
| Django - HelloWorld | 2205.60 | 7.15ms | 116.67 | 201843 |
| Django - Fibonacci(25) | 8.33 | 5.93ms | 1.53 | 255149 |
| Spring - HelloWorld | 509.15 | 282.78us | 4.34 | 86974 |
| Spring - Fibonacci(25) | 35603.87 | 1.22ms | 949.67 | 168138 |
