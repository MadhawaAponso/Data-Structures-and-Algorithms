def fibonacci(n):
    assert n >0 and int(n)==n , "N must not be negative or Non integer"
    if n == 1 or n == 0:
        return n
    else:
        return fibonacci(n-1)+ fibonacci(n-2)

print(fibonacci(6))