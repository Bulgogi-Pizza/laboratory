# 개요

우리가 프로젝트를 시작할 때 FastAPI, Express.js, Django, Spring의 다양한 백엔드 프레임워크 중에서 생산성, 성능, 유지보수성, 안정성 등 다양한 부분을 고려하고 선택하게 된다. 최근 대부분의 스타트업에서는 빠른 개발을 위한 FastAPI, 풀스택 개발을 위한 Express.js를 주로 선택하고 있는데, 오늘은 생산성과 유지보수성이 아닌 성능의 측면에서 각 프레임워크를 비교해보고자 한다.

## 프레임워크 소개

- FastAPI (Python)
    - 이름처럼 빠른 API를 만드는 데 특화된 파이썬 프레임워크
    - 현대적이며 비동기 방식을 지원해서 성능이 뛰어나고 코드 작성도 간편하다
- Express.js (Node.js/JavaScript)
    - Node.js 환경에서 가장 인기 있는 경량 프레임워크
    - 유연성이 높고, 비동기 I/O 처리 덕분에 빠른 응답 속도를 보장
- Django (Python)
    - 배터리 포함(Batteries-included) 철학을 가진 파이썬 프레임워크
    - 개발에 필요한 대부분의 기능(관리자 페이지, ORM 등)이 내장되어 있어 크고 복잡한 웹 애플리케이션을 빠르게 만들 수 있음
- Spring (Java)
    - 자바 기반의 대표적인 프레임워크
    - 특히 대규모 기업용 애플리케이션 개발에 많이 쓰임, 안정성과 확장성이 매우 뛰어남

## 각 프레임워크의 사용처

- FastAPI
    - 마이크로서비스, 실시간 API, 머신러닝 모델 서빙
    - →  빠른 성능, 자동 API 문서화, 쉬운 비동기 처리
- Express
    - 마이크로서비스, 단일 페이지 애플리케이션의 백엔드, 실시간 앱
    - → 높은 유연성, 거대한 JavaScript 생태계(npm), 빠른 I/O
- Django
    - 콘텐츠 관리 시스템(CMS), 복잡한 데이터 기반의 웹사이트, 관리자 페이지가 중요한 프로젝트
    - → Batteries-included 철학으로 빠른 개발 가능
- Spring
    - 대규모 기업용 시스템(금융, 이커머스), 높은 안정성과 보안이 요구되는 시스템
    - → 강력한 생태계, 안정성, 뛰어난 확장성

| 프레임워크 | 언어 | 핵심 아키텍처 | 처리 방식 |
| --- | --- | --- | --- |
| FastAPI | Python | ASGI (비동기) | 이벤트 루프 기반, 비동기 |
| Express | Node.js | 이벤트 루프 (비동기) | 싱글 스레드, 비동기 I/O |
| Django | Python | WSGI (동기) | 요청당 스레드/프로세스, 동기 |
| Spring | Java | 서블릿 컨테이너 | 멀티 스레드, 동기 (WebFlux로 비동기도 지원) |

가장 큰 차이점은 동기와 비동기 처리 방식의 차이이다.

Django와 Spring의 기본 동작 방식이 동기 방식이고, FastAPI와 Express의 기본 동작 방식이 비동기 방식이다. 

## 일반적으로 알려진 성능 벤치마크 결과

### 단순 API 요청 처리 (I/O 위주)

1. FastAPI / Express.js (최상위권): 비동기 아키텍처 덕분에 매우 높은 처리량(TPS)과 낮은 지연 시간을 보여준다.
2. Spring (WebFlux): 비동기 모델을 사용할 경우 FastAPI, Express와 비슷한 성능을 낼 수 있다.
3. Django / Spring (기본 MVC): 동기 방식의 한계로 앞선 프레임워크들보다는 처리량이 낮게 측정되는 경우가 많다.

### CPU 연산 위주 작업

이 때는 언어 자체의 성능이 중요해진다. 컴파일 언어인 Java(Spring)가 인터프리터 언어인 Python(Django, FastAPI)이나 JavaScript(Express)보다 유리할 수 있다.

## 성능 비교 지표

- Throughput (처리량): 서버가 일정 시간 동안 얼마나 많은 요청을 처리할 수 있는가 (단위: TPS, RPS)
- Latency (지연 시간): 요청을 보낸 후 응답을 받기까지 걸리는 시간은 얼마나 짧은가
- Memory Usage (메모리 사용량): 프레임워크가 동작하는 데 얼마나 많은 메모리를 사용하는가

# Test 1 (Normal)

| **테스트 시나리오** | **TPS (요청/초)** | **평균 Latency** | **평균 CPU (%)** | **평균 Memory (KB)** |
| --- | --- | --- | --- | --- |
| FastAPI - HelloWorld | 7092.83 | 14.45ms | 88.07 | 37862 |
| FastAPI - Fibonacci(25) | 71.37 | 276.75ms | 100.28 | 42348 |
| Express - HelloWorld | 17992.43 | 6.33ms | 98.25 | 97570 |
| Express - Fibonacci(25) | 1798.19 | 11.19ms | 101.50 | 107338 |
| Django - HelloWorld | 3400.46 | 28.99ms | 97.37 | 50469 |
| Django - Fibonacci(25) | 84.82 | 14.50ms | 0.69 | 51286 |
| Spring - HelloWorld | 115883.67 | 793.10us | 735.94 | 178210 |
| Spring - Fibonacci(25) | 34384.58 | 614.76us | 992.59 | 197569 |

### Spring의 CPU 사용량이 100%를 넘는 이유

Spring은 완전한 멀티스레딩을 지원한다. 하나의 프로세스 안에서 수많은 스레드를 생성해 여러 CPU 코어에 작업을 분산시키는 데 매우 효율적이다. 이 때문에 하드웨어의 성능을 최대한으로 끌어낼 수 있고, CPU 사용률이 100%를 넘을 수 있는 것이다. (100% → 1코어 완전히 사용 중, 300% → 3코어 완전히 사용 중)

그에 반해 Express는 싱글 스레드 이벤트 루프 모델을 기반으로 한다. 핵심 작업은 하나의 CPU 코어에서 처리되므로, CPU 사용률이 100% 근처에서 한계를 보인다.

Python(FastAPI/Django)의 경우 파이썬의 GIL(Global Interpreter Lock)이라는 제약 때문에, 하나의 프로세스는 한 번에 하나의 CPU 코어만 사용하여 파이썬 코드를 실행할 수 있다. 이 때문에 CPU 사용률이 100% 근처에 머물게 된다.

결론적으로 Spring의 높은 CPU 수치는 하드웨어를 가장 효율적으로 활용하여 병렬 처리 성능을 극대화했다는 신호로 해석할 수 있다.

### 모두 단일 스레드로 동작하게 하기

Spring

- [application.properties](http://application.properties) 파일에 `server.tomcat.threads.max=1`로 설정해 톰캣이 요청을 처리하는 최대 스레드 수를 1로 제한하면 된다.

| **테스트 시나리오** | **TPS (요청/초)** | **평균 Latency** | **평균 CPU (%)** | **평균 Memory (KB)** |
| --- | --- | --- | --- | --- |
| FastAPI - HelloWorld | 7073.17 | 14.42ms | 88.17 | 38050 |
| FastAPI - Fibonacci(25) | 71.53 | 278.22ms | 99.76 | 41932 |
| Express - HelloWorld | 17947.70 | 6.36ms | 99.00 | 96970 |
| Express - Fibonacci(25) | 1803.85 | 11.16ms | 101.73 | 106173 |
| Django - HelloWorld | 3581.17 | 27.05ms | 94.82 | 50456 |
| Django - Fibonacci(25) | 115.58 | 17.04ms | 2.03 | 51611 |
| Spring - HelloWorld | 21335.64 | 4.68ms | 106.77 | 74336 |
| Spring - Fibonacci(25) | 4506.14 | 4.43ms | 105.77 | 82430 |

### 모두 멀티 스레드로 동작하게 하기

FastAPI

- uvicorn 실행 시 명령어를 `uvicorn main:app --host 0.0.0.0 --port 8000 --workers [n]`으로 설정해 최대 워커 수를 늘릴 수 있다.

Django

- `python [manage.py](http://manage.py) runserver` 명령어는 개발용 단일 스레드 서버이므로 실제 서비스 환경처럼 Gunicorn을 사용하면 여러 워커 프로세스를 실행해 멀티 코어를 온전히 활용할 수 있다.
    1. `pip install gunicorn`
    2. `gunicorn --workers [n] --bind 0.0.0.0:8002 laboratory.wsgi`

Express

- 코드를 직접 수정해 클러스터 모드를 적용해야 한다.
- `index.js`는 그대로 두고, 클러스터 로직을 담은 `cluster.js` 파일을 새로 만든다.
- `cluster.js` 코드 전문
    
    ```jsx
    const cluster = require('cluster');
    const os = require('os');
    
    if (cluster.isMaster) {
      const cpuCount = os.cpus().length;
      console.log(`마스터 프로세스 (PID: ${process.pid}) 실행 중`);
      console.log(`${cpuCount}개의 CPU 코어를 활용하여 워커를 생성합니다.`);
    
      for (let i = 0; i < cpuCount; i++) {
        cluster.fork();
      }
    
      cluster.on('exit', (worker, code, signal) => {
        console.log(`${worker.process.pid}번 워커가 종료되었습니다. 새로운 워커를 생성합니다.`);
        cluster.fork();
      });
    } else {
      // 워커 프로세스들은 기존의 index.js 파일을 실행합니다.
      require('./index.js');
    }
    ```
    
- 이렇게 하면, 워커 프로세스들이 생성되고 각 워커 프로세스들은 기존의 index.js 파일을 실행하도록 할 수 있다.
- 그 후 `node cluster.js`로 실행하면 된다.

| **테스트 시나리오** | **TPS (요청/초)** | **평균 Latency** | **총 CPU 사용량 (%)** | **총 메모리 사용량 (KB)** |
| --- | --- | --- | --- | --- |
| FastAPI - HelloWorld | 25113.63 | 5.75ms | 659.98 | 307293 |
| FastAPI - Fibonacci(25) | 623.36 | 32.04ms | 1051.02 | 315754 |
| Express - HelloWorld | 107836.51 | 1.67ms | 835.98 | 920486 |
| Express - Fibonacci(25) | 14617.08 | 1.45ms | 1080.85 | 1058051 |
| Django - HelloWorld | 2169.13 | 7.18ms | 119.89 | 303354 |
| Django - Fibonacci(25) | 0.10 | 3.44ms | 0.12 | 336592 |
| Spring - HelloWorld | 583.93 | 388.44us | 3.62 | 101979 |
| Spring - Fibonacci(25) | 4824.40 | 282.65us | 83.52 | 146824 |
| Spring - HelloWorld (NM) | 116109.49 | 797.13us | 751.75 | 171044 |
| Spring - Fibonacci(25) (NM) | 33581.76 | 615.91us | 964.01 | 189472 |

# 결론

- Express는 비동기 I/O 부분에서 압도적인 성능을 보인다. 단순 요청(HelloWorld) 처리 속도를 보면 알 수 있다.
- Spring은 CPU 연산에서 압도적인 성능을 보인다. 순수 연산 능력과 멀티코어 활용 능력이 압도적이다.
- Python 프레임워크는 생각보다 지지부진한 모습을 보이며 생산성과 성능 사이의 트레이드오프를 여실히 보여준다고 생각한다. 눈에 띄는 모습으로는, FastAPI가 Django에 비해 평균 두배의 성능을 내고 있는 것이 흥미롭다.
- Django는 멀티 스레드 테스트가 제대로 진행된 것 같지 않아 아쉽다.

## Express - 왜 이렇게 빠른가?

- HellloWorld (I/O 작업): 싱글, 멀티 모든 시나리오에서 압도적인 TPS
    - Node.js의 V8 엔진과 `libuv`를 기반으로 한 비동기 이벤트 루프 모델이 이 분야의 최강자이기 때문이다. 요청이 들어오면 작업을 던져놓고 즉시 다음 요청을 받을 준비를 하므로, 대기 시간이 거의 없는 단순 I/O 작업에서 엄청난 처리랴을 보여준다. Express는 프레임워크 자체도 매우 가벼워 오버헤드가 거의 없는 점도 큰 장점이다.
- Fibonacci (CPI 작업): 여기서도 매우 뛰어난 성능을 보인다.
    - V8 엔진의 JIT(Just-In-Time) 컴파일러가 자바스크립트 코드를 매우 효율적으로 최적화해 주기 때문에 빠르다. 멀티프로세스(클러스터 모드)로 확장했을 때 CPU 사용량이 1000%를 넘어가며 여러 코어를 효과적으로 활용해 성능을 끌어올리는 모습을 명확히 보여준다.

## Spring - CPU 연산은 최고, 그러나

- Fibonacci (CPU 작업): 멀티스레드에서 압도적인 1위
    - JVM의 JIT 컴파일러 덕분이다. Java 코드는 실행 중 JVM에 의해 지속적으로 분석되고, 자주 사용되는 Hot 코드 블록(여기서는 피보나치 재귀 함수)은 극도로 최적화된 네이티브 머신 코드로 변환된다. 이 과정 덕분에 순수 연산 속도는 인터프리터 언어인 파이선이나 자바스크립트를 훨씬 뛰어넘는다.
- HelloWorld (I/O 작업): 기본 설정에서는 Express보다 훨씬 빠르고, 싱글 스레드는 Express보다 느리다.
    - Spring은 Express보다 훨씬 무거운 프레임워크이다. 수많은 기능이 내장되어 있어 요청 처리의 기본 오버헤드가 크다. 기본 설정에서는 강력한 멀티스레딩으로 이 오버헤드를 찍어 누르며 높은 성능을 낸다.

## Python (FastAPI & Django) - 명확한 트레이드오프

- FastAPI
    - 전반적으로 Django보다 훨씬 뛰어난 성능을 보여준다. 비동기의 힘이라고 할 수 있다. 멀티 워커로 확장했을 때 1000%까지 올라가며 여러 코어를 잘 활용하는 모습도 보여주지만, Express의 경량 비동기 모델이나 Spring의 네이티브급 연산 속도에는 미치지 못한다.
- Django
    - 가장 낮은 성능을 기록했다.
    - 이유 1 (동기 방식): Gunicorn 워커는 동기 방식이라 I/O 대기 중에 다른 요청을 처리하지 못하고 멈춰있다. 이것이 TPS가 낮은 가장 큰 이유이다.
    - 이유 2 (오버헤드): 프레임워크 자체가 무겁다. 개발 생산성을 위해 수많은 기능을 내장한 대가로, 순수 성능에서는 손해를 본다.

## Python이 생각보다 성능이 좋지 않다.

- 순수 성능 벤치마크에서 Python은 컴파일 언어나 최적화된 런타임에 비해 불리하다. 그럼에도 불구하고 Python을 사용하는 이유는 개발 생산성에 있다. 간결한 문법, 라이브러리 생태계는 개발 속도를 비약적으로 높여준다. FastAPI는 이 생산성을 유지하면서 비동기를 통해 성능을 크게 끌어올린 좋은 예시이다.

## Express와 Spring의 성능이 엄청 좋다.

- 각자의 주력 분야에서 엄청난 성능을 보여준다.
- Express는 수많은 동시 접속과 짧은 I/O가 반복되는 MSA, 채팅 앱, API 게이트웨이 등에서 발군의 성능을 보인다.
- Spring은 복잡한 비즈니스 로직, 대규모 데이터 처리, 안정적인 백그라운드 연산이 필요한 금융 시스템, 대규모 이커머스, 엔터프라이즈 애플리케이션에서 그 진가를 발휘한다.

- 가볍고 빠른 API 서버가 필요하다면 **Express**가 훌륭한 선택이다.
- 개발 속도와 방대한 기능이 중요하다면 **Django**가 여전히 매력적이다.
- Django의 생산성은 유지하면서 더 나은 성능을 원한다면 **FastAPI**가 좋은 대안이다.
- 복잡하고 무거운 연산과 최고의 안정성이 필요하다면 **Spring**이 가장 신뢰할 수 있는 선택지이다.
