# 종합 성능 테스트 결과

| 테스트 시나리오 | TPS (요청/초) | 평균 Latency | 평균 CPU (%) | 평균 Memory (KB) |
|---|---|---|---|---|
| FastAPI - HelloWorld | 7040.18 | 14.62ms | 88.05 | 37998 |
| FastAPI - Fibonacci(25) | 71.45 | 275.60ms | 99.57 | 42679 |
| Express - HelloWorld | 17987.08 | 6.37ms | 99.91 | 96607 |
| Express - Fibonacci(25) | 1799.91 | 11.19ms | 101.30 | 105296 |
| Django - HelloWorld | 3573.32 | 27.22ms | 94.92 | 51574 |
| Django - Fibonacci(25) | 64.82 | 10.91ms | 2.79 | 52099 |
| Spring - HelloWorld | 21837.85 | 4.58ms | 107.82 | 73232 |
| Spring - Fibonacci(25) | 4534.10 | 4.41ms | 105.67 | 81518 |
