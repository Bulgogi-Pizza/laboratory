# 종합 성능 테스트 결과

| 테스트 시나리오 | TPS (요청/초) | 평균 Latency | 평균 CPU (%) | 평균 Memory (KB) |
|---|---|---|---|---|
| FastAPI - HelloWorld | 7005.17 | 14.76ms | 86.29 | 38237 |
| FastAPI - Fibonacci(25) | 69.67 | 280.56ms | 100.41 | 41702 |
| Express - HelloWorld | 18007.79 | 6.45ms | 99.15 | 97805 |
| Express - Fibonacci(25) | 1802.50 | 11.20ms | 101.38 | 106646 |
| Django - HelloWorld | 3528.18 | 27.54ms | 94.96 | 50458 |
| Django - Fibonacci(25) | 122.78 | 17.24ms | 1.99 | 51350 |
| Spring - HelloWorld | 115053.03 | 795.97us | 730.15 | 170810 |
| Spring - Fibonacci(25) | 33839.09 | 622.65us | 959.73 | 189673 |
