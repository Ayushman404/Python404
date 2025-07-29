n = 5

def factorial(n):
    result = 1
    while n > 1:
        result *= n
        n -= 1
    
    return result

print(f"The factorial of {n} is {factorial(n)}")