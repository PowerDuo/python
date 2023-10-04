# Code submitted by SUGAM KUMAR SINGH
# UID: 20BCS5820

# declaring and initializing a variable to store sum of marks
sum = 0

# creating a for loop to take input for 5 subjects
for i in range(5):
    
    # taking input one by one for all subjects
    marksInput = int(input("Enter marks in subject " + str(i+1) + " : "))

    # adding the marks to sum variable for calculating average and percentage later
    sum += marksInput
    
print("\n-----\t ASSUMING MARKS OUT OF 100 \t-----")

# type casting the int/float to str, before concatenating and printing it
print("Sum of all the marks is: " + str(sum))
print("Average marks are: " + str(sum/5))
print("Percentage is: " + str(sum/5) + "%")