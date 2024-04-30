# Using different way instead of using choice() function
import random

names_string = input("Give me everybody's names, separated by a comma: ")
names = names_string.split(", ")
# Generate random numbers between 0 and the last index
random_choice = random.randint(0, len(names)-1)
person_who_pay = names[random_choice]
print(f"{names[random_choice]} is going to buy the meal today!")