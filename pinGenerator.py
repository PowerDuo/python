import random

n = int(input("Enter the length of the password: "))
for i in range(n):
    print(random.randint(0, 10), end="")