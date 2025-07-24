# 종합 성능 테스트 결과

| 테스트 시나리오 | TPS (요청/초) | 평균 Latency | 평균 CPU (%) | 평균 Memory (KB) |
|---|---|---|---|---|
| FastAPI - HelloWorld | 7073.17 | 14.42ms | 88.17 | 38050 |
| FastAPI - Fibonacci(25) | 71.53 | 278.22ms | 99.76 | 41932 |
| Express - HelloWorld | 17947.70 | 6.36ms | 99.00 | 96970 |
| Express - Fibonacci(25) | 1803.85 | 11.16ms | 101.73 | 106173 |
| Django - HelloWorld | 3581.17 | 27.05ms | 94.82 | 50456 |
| Django - Fibonacci(25) | 115.58 | 17.04ms | 2.03 | 51611 |
| Spring - HelloWorld | 21335.64 | 4.68ms | 106.77 | 74336 |
| Spring - Fibonacci(25) | 4506.14 | 4.43ms | 105.77 | 82430 |
