print("The Love Calculator is calculating your score...")
name1 = input() # What is your name?
name2 = input() # What is your partner's name?

combined_names = name1 + name2
lover_names = combined_names.lower()
t = lover_names.count("t")
r = lover_names.count("r")
u = lover_names.count("u")
e = lover_names.count("e")
first_digit = t + r + u + e
l = lover_names.count("l")
o = lover_names.count("o")
v = lover_names.count("v")
e = lover_names.count("e")
second_digit = l + o + v + e
love_score = int (str(first_digit)+ str(second_digit))

if (love_score < 10) or (love_score > 90):
  print(f"Your score is {love_score}, you go together like coke and mentos.")
elif (love_score >= 40) and (love_score <= 50):
  print(f"Your score is {love_score}, you are alright together.")
else:
  print(f"Your score is {love_score}.")
