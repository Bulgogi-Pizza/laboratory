# venv 활성화
```
# Mac
source .venv/bin/activate
```

# 의존성 설치
```
pip install fastapi "uvicorn[standard]"
```

# 실행
```
uvicorn main:app --host 0.0.0.0 --port 8000
```

# venv 비활성화
```
deactivate
```