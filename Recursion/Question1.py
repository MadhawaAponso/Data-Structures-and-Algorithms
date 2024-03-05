# How to find the sum of digits of a positive number using recursion.

def sum_digits(number):
    if(number <=0):
        return number
    else: 
        return (number % 10) + sum_digits(number // 10)

print(sum_digits(11111111))