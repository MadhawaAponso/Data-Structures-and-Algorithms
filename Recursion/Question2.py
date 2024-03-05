#How to calculate the power of a number using recursion

def power(m,n):
    assert int(n)==n , "Exponent must be integer"
    if n == 0:
        return 1
    elif n<0:
        return 1/m*power(m,n+1)
    else:return m * power(m,n-1)

print(power(2,-3))