#python program to calculate the factorial of a number
#this is a recursive method to calculate factorial i.e uses recursion

def factorial(n):

    #returns 1 is the number entered is 1
    if n == 1:
        return 1
        
    #returns the product of the number with its decrement by 1
    else:
        return n * factorial(n-1)

m = int(input('Enter number whose factorial you wish to calculate: '))
print(factorial(m))
