# -*- coding: utf-8 -*-
"""
@author: Nellman1508
"""

user_number = 0
cycle_counter = -1
intermediate_number = 0
intermediate_number_list = []
squared_digit_lsit = []
cycle_start = 0
user_input = input("Please enter a natural number: ")


try:
    user_number = int(user_input)
except:
    raise SystemError("Wrong input, please try again")

if user_number <= 0:
    raise SystemError("Wrong input, not a natural Number.")

intermediate_number = user_number
intermediate_number_list.append(user_number)

while intermediate_number != 1:
    cycle_counter += 1
    squared_digit_lsit = []
    for digit in range(0, len(str(intermediate_number))):
        squared_digit_lsit.append(int(str(intermediate_number)[digit]) ** 2)

    intermediate_number = sum(squared_digit_lsit)
    intermediate_number_list.append(intermediate_number)
    if cycle_counter == 100:
        print("Aborted after 100 cycles, took too long.")
        break


    if intermediate_number in intermediate_number_list[1:-1]:
        print("The number creates a harmonic cycle.",
              "The calculation was aborted after ", cycle_counter,
              " cycles.")
        cycle_start = intermediate_number_list.index(intermediate_number)
        print("The cycle is: ", intermediate_number_list[cycle_start:-1])
        break

if intermediate_number == 1:
    print("The number is a happy number.")

print("Intermediary resulats are:\n11", intermediate_number_list)
