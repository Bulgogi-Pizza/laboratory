from django.http import JsonResponse

def hello_world(request):
    return JsonResponse({"message": "Hello, World!"})

def fibonacci(n: int) -> int:
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)

def calculate_fib(request, number):
    result = fibonacci(number)
    return JsonResponse({"number": number, "fibonacci": result})