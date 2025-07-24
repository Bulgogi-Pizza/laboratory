# 종합 성능 테스트 결과

| 테스트 시나리오 | TPS (요청/초) | 평균 Latency | 평균 CPU (%) | 평균 Memory (KB) |
|---|---|---|---|---|
| FastAPI - HelloWorld | 7044.27 | 14.37ms | 87.89 | 38392 |
| FastAPI - Fibonacci(25) | 70.01 | 278.34ms | 99.96 | 41274 |
| Express - HelloWorld | 18077.33 | 6.48ms | 99.21 | 96276 |
| Express - Fibonacci(25) | 1809.91 | 11.13ms | 101.04 | 105014 |
| Django - HelloWorld | 3611.18 | 27.02ms | 94.72 | 51299 |
| Django - Fibonacci(25) | 216.80 | 17.86ms | 12.09 | 52427 |
| Spring - HelloWorld | 21650.66 | 4.60ms | 107.37 | 72506 |
| Spring - Fibonacci(25) | 4457.45 | 4.48ms | 105.72 | 79573 |
