line1 = ["⬜️","️⬜️","️⬜️"]
line2 = ["⬜️","⬜️","️⬜️"]
line3 = ["⬜️️","⬜️️","⬜️️"]
map = [line1, line2, line3]
print("Hiding your treasure! X marks the spot.")
position = input("Where do you want to put the treasure? ")
# The first char of the position is the letter, the second is the number
letter = position[0].lower()
abc = ["a", "b", "c"]
# Convert the letter to an index
letter_index = abc.index(letter)
# Convert the number to an index
number_index = int(position[1]) - 1
# Update the map to shoe the treasure
map[number_index][letter_index] = 'X'

print(f"{line1}\n{line2}\n{line3}")