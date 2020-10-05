def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n-1)

m = int(input('Enter number whose factorial you wish to calculate: '))
print(factorial(m))
