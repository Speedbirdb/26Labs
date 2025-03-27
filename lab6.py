call_count = 0
sum = 0.0

def func(n):
    global call_count, sum
    call_count += 1

    sum += 1.0 / n

    """Base case"""
    if(n == 1):
        print(f"Summation : {sum}")
        return
    
    func(n-1)


def factorial(x):
    if x < 0:
        raise ValueError("Factorial is not defined for negative numbers")
    if x == 0 or x == 1:
        return 1
    
    return x * factorial(x - 1)