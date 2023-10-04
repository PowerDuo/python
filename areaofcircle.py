# Code submitted by SUGAM KUMAR SINGH
# UID: 20BCS5820

pie = 22/7

def circleAreaBySimpleFunction():
    r = float(input("Enter radius of the circle: "))
    print(pie * r * r)

def circleAreaByParameterizedFunction(r):
    print(pie * r * r)

def circleAreaBySimpleReturnFunction():
    r = float(input("Enter radius of the circle: "))
    return(pie * r * r)

def circleAreaByParameterizedReturnFunction(r):
    return(pie * r * r)

print("\n----- Area of circle by simple function -----")
circleAreaBySimpleFunction()

print("\n----- Area of circle by parameterized function -----")
circleAreaByParameterizedFunction(3)

print("\n----- Area of circle by simple return function -----")
print(circleAreaBySimpleReturnFunction())

print("\n----- Area of circle by parameterized return function -----")
print(circleAreaByParameterizedReturnFunction(7))