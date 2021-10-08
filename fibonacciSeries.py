x=int(input("How many terms you want to print: "))
a = int(0)
b = int(1)
print (a)
print (b)
c = int(a+b)
i = 1
while i < x:
    print (c)
    a = b
    b = c
    c = (a+b)
    i += 1

input("Press enter to exit")