import random
 
min_value = 1
max_value = 6
 
roll = True
 
while again:
    print(random.randint(min_value, max_value))
 
    another_roll = input('Want to roll the dice again? \n\nY/y or yes to roll again \n ')
 
    if another_roll == 'yes' or another_roll == 'y' or another_roll == 'Y':
        again = True
    else:
        again = False
