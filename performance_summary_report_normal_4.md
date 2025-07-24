# 종합 성능 테스트 결과

| 테스트 시나리오 | TPS (요청/초) | 평균 Latency | 평균 CPU (%) | 평균 Memory (KB) |
|---|---|---|---|---|
| FastAPI - HelloWorld | 6991.19 | 14.75ms | 88.08 | 37723 |
| FastAPI - Fibonacci(25) | 71.62 | 276.07ms | 98.02 | 41895 |
| Express - HelloWorld | 18122.06 | 6.35ms | 98.98 | 97777 |
| Express - Fibonacci(25) | 1804.26 | 11.17ms | 101.71 | 106114 |
| Django - HelloWorld | 3597.40 | 27.10ms | 94.81 | 51062 |
| Django - Fibonacci(25) | 38.37 | 17.08ms | 0.55 | 51662 |
| Spring - HelloWorld | 116109.49 | 797.13us | 751.75 | 171044 |
| Spring - Fibonacci(25) | 33581.76 | 615.91us | 964.01 | 189472 |
