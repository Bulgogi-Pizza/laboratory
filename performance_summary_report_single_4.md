# 종합 성능 테스트 결과

| 테스트 시나리오 | TPS (요청/초) | 평균 Latency | 평균 CPU (%) | 평균 Memory (KB) |
|---|---|---|---|---|
| FastAPI - HelloWorld | 6957.33 | 15.31ms | 87.35 | 37686 |
| FastAPI - Fibonacci(25) | 69.96 | 279.18ms | 100.05 | 41146 |
| Express - HelloWorld | 18030.19 | 6.40ms | 99.26 | 97495 |
| Express - Fibonacci(25) | 1803.92 | 11.16ms | 100.77 | 106245 |
| Django - HelloWorld | 3583.83 | 27.31ms | 94.68 | 51064 |
| Django - Fibonacci(25) | 73.85 | 17.40ms | 1.91 | 51602 |
| Spring - HelloWorld | 21480.05 | 4.64ms | 107.34 | 73270 |
| Spring - Fibonacci(25) | 4454.05 | 4.48ms | 105.44 | 79126 |
