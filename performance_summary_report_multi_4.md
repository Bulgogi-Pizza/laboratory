# 종합 성능 테스트 결과 (멀티프로세스 자원 합산)

| 테스트 시나리오 | TPS (요청/초) | 평균 Latency | 총 CPU 사용량 (%) | 총 메모리 사용량 (KB) |
|---|---|---|---|---|
| FastAPI - HelloWorld | 24553.80 | 6.36ms | 655.31 | 312754 |
| FastAPI - Fibonacci(25) | 616.00 | 33.06ms | 1031.50 | 306405 |
| Express - HelloWorld | 108583.18 | 1.63ms | 846.44 | 918864 |
| Express - Fibonacci(25) | 14464.38 | 1.55ms | 1089.69 | 1054379 |
| Django - HelloWorld | 2412.16 | 7.19ms | 129.00 | 263125 |
| Django - Fibonacci(25) | 17.24 | 5.78ms | 1.88 | 314312 |
| Spring - HelloWorld | 2355.69 | 635.36us | 14.13 | 143957 |
| Spring - Fibonacci(25) | 2731.04 | 320.35us | 36.20 | 157922 |
