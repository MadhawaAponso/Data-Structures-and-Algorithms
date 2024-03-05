def factorial(n):
    assert n>=1 and int(n)==n , "The n must be positive whole interger"
    if n == 0 or n == 1:
        return 1
    else: 
        ans = n*factorial(n-1)
        return ans


print(factorial(2.4))


