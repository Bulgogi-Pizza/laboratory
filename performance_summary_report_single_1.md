# 종합 성능 테스트 결과

| 테스트 시나리오 | TPS (요청/초) | 평균 Latency | 평균 CPU (%) | 평균 Memory (KB) |
|---|---|---|---|---|
| FastAPI - HelloWorld | 6997.49 | 14.48ms | 88.56 | 38032 |
| FastAPI - Fibonacci(25) | 71.27 | 277.01ms | 99.61 | 40407 |
| Express - HelloWorld | 18060.99 | 6.36ms | 99.19 | 97063 |
| Express - Fibonacci(25) | 1802.97 | 11.17ms | 101.05 | 105776 |
| Django - HelloWorld | 3590.80 | 27.02ms | 95.02 | 50763 |
| Django - Fibonacci(25) | 157.83 | 17.40ms | 1.79 | 51832 |
| Spring - HelloWorld | 21005.18 | 5.25ms | 108.14 | 125341 |
| Spring - Fibonacci(25) | 4371.40 | 5.08ms | 105.66 | 136666 |
