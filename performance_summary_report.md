# 종합 성능 테스트 결과 (멀티프로세스 자원 합산)

| 테스트 시나리오 | TPS (요청/초) | 평균 Latency | 총 CPU 사용량 (%) | 총 메모리 사용량 (KB) |
|---|---|---|---|---|
| FastAPI - HelloWorld | 25019.96 | 5.49ms | 648.63 | 294539 |
| FastAPI - Fibonacci(25) | 623.66 | 33.82ms | 1029.04 | 300045 |
| Express - HelloWorld | 107416.11 | 1.66ms | 809.76 | 916568 |
| Express - Fibonacci(25) | 13886.85 | 1.80ms | 983.05 | 1050267 |
| Django - HelloWorld | 2435.01 | 7.10ms | 118.90 | 222869 |
| Django - Fibonacci(25) | 26.65 | 4.66ms | 4.03 | 277333 |
| Spring - HelloWorld | 5743.06 | 820.67us | 23.97 | 153696 |
| Spring - Fibonacci(25) | 4171.52 | 313.68us | 56.67 | 168302 |
