# 종합 성능 테스트 결과 (멀티프로세스 자원 합산)

| 테스트 시나리오 | TPS (요청/초) | 평균 Latency | 총 CPU 사용량 (%) | 총 메모리 사용량 (KB) |
|---|---|---|---|---|
| FastAPI - HelloWorld | 24748.21 | 5.76ms | 645.98 | 309802 |
| FastAPI - Fibonacci(25) | 622.30 | 32.17ms | 1039.00 | 291750 |
| Express - HelloWorld | 107840.80 | 1.69ms | 833.94 | 919746 |
| Express - Fibonacci(25) | 14822.05 | 1.47ms | 1081.89 | 1057555 |
| Django - HelloWorld | 2143.66 | 7.20ms | 116.67 | 204736 |
| Django - Fibonacci(25) | 0.20 | 3.81ms | 0.23 | 223846 |
| Spring - HelloWorld | 1017.66 | 514.48us | 5.49 | 127736 |
| Spring - Fibonacci(25) | 34086.07 | 1.63ms | 855.59 | 154358 |
