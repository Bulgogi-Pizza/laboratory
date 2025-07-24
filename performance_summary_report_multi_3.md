# 종합 성능 테스트 결과 (멀티프로세스 자원 합산)

| 테스트 시나리오 | TPS (요청/초) | 평균 Latency | 총 CPU 사용량 (%) | 총 메모리 사용량 (KB) |
|---|---|---|---|---|
| FastAPI - HelloWorld | 25113.63 | 5.75ms | 659.98 | 307293 |
| FastAPI - Fibonacci(25) | 623.36 | 32.04ms | 1051.02 | 315754 |
| Express - HelloWorld | 107836.51 | 1.67ms | 835.98 | 920486 |
| Express - Fibonacci(25) | 14617.08 | 1.45ms | 1080.85 | 1058051 |
| Django - HelloWorld | 2169.13 | 7.18ms | 119.89 | 303354 |
| Django - Fibonacci(25) | 0.10 | 3.44ms | 0.12 | 336592 |
| Spring - HelloWorld | 583.93 | 388.44us | 3.62 | 101979 |
| Spring - Fibonacci(25) | 4824.40 | 282.65us | 83.52 | 146824 |
