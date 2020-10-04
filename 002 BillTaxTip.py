#This program was uploaded to HackerRank on Day 1 of 30 Days of Code

meal_price=float(input("mealCost"))         # HackerRank was displaying me error
tip_percentage=int(input("tipPercent"))     # so as to remove that error
tax_percentage=int(input("taxPercent"))     # clear input text

tip=meal_price*0.01*tip_percentage
tax=meal_price*0.01*tax_percentage

total=meal_price+tip+tax
bill=round(total)

print (bill)