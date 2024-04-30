target = int(input("Enter a number between 0 and 1000: "))

sum_of_even_number = 0
for number in range(0, target + 1, 2):
  sum_of_even_number += number
print(sum_of_even_number)

# Second way:

# sum_of_even_number = 0
# for number in range(0, target + 1):
#     if number % 2 ==0:
#         sum_of_even_number += number
# print(sum_of_even_number)