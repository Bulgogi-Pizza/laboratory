# 종합 성능 테스트 결과

| 테스트 시나리오 | TPS (요청/초) | 평균 Latency | 평균 CPU (%) | 평균 Memory (KB) |
|---|---|---|---|---|
| FastAPI - HelloWorld | 7049.94 | 14.72ms | 87.63 | 37723 |
| FastAPI - Fibonacci(25) | 71.48 | 276.07ms | 100.03 | 41281 |
| Express - HelloWorld | 17856.18 | 6.75ms | 99.22 | 96381 |
| Express - Fibonacci(25) | 1806.93 | 11.14ms | 101.62 | 106128 |
| Django - HelloWorld | 3537.49 | 27.70ms | 93.81 | 50816 |
| Django - Fibonacci(25) | 88.15 | 14.92ms | 1.81 | 50963 |
| Spring - HelloWorld | 115650.60 | 779.82us | 729.40 | 178990 |
| Spring - Fibonacci(25) | 33695.49 | 618.75us | 960.57 | 202701 |
