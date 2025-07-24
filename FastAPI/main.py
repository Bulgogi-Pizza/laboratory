from fastapi import FastAPI

app = FastAPI()

def fibonacci(n: int) -> int:
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)
@app.get("/")
def read_root():
    return {"message": "Hello, World!"}

@app.get("/calculate/{number}")
def calculate_fib(number: int):
    result = fibonacci(number)
    return {"number": number, "fibonacci": result}