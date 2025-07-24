# 종합 성능 테스트 결과

| 테스트 시나리오 | TPS (요청/초) | 평균 Latency | 평균 CPU (%) | 평균 Memory (KB) |
|---|---|---|---|---|
| FastAPI - HelloWorld | 7092.83 | 14.45ms | 88.07 | 37862 |
| FastAPI - Fibonacci(25) | 71.37 | 276.75ms | 100.28 | 42348 |
| Express - HelloWorld | 17992.43 | 6.33ms | 98.25 | 97570 |
| Express - Fibonacci(25) | 1798.19 | 11.19ms | 101.50 | 107338 |
| Django - HelloWorld | 3400.46 | 28.99ms | 97.37 | 50469 |
| Django - Fibonacci(25) | 84.82 | 14.50ms | 0.69 | 51286 |
| Spring - HelloWorld | 115883.67 | 793.10us | 735.94 | 178210 |
| Spring - Fibonacci(25) | 34384.58 | 614.76us | 992.59 | 197569 |
