# 1st input: enter height in meters e.g: 1.65
height = input("Enter your height in meteres: ")
# 2nd input: enter weight in kilograms e.g: 72
weight = input("Enter your weight in kg: ")

digit_height = float(height)
digit_weight = float(weight)
BMI = digit_weight / (digit_height ** 2)
print(int(BMI))