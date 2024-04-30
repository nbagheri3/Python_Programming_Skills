import random
from hangman_art import logo,stages
from hangman_words import word_list

print(logo)

end_of_game = False
chosen_word = random.choice(word_list)
length_word = len(chosen_word)

lives = 6
#Testing code
print(f'Psssss the solution is: {chosen_word}')

#Create blanks
display = []
for _ in range(length_word):
    display += "_"

while not end_of_game:
    guess = input("Guess a letter: ").lower()


    if guess in display:
        print(f"You've already guessed {guess}")
    # Check guessed letter
    for position in range(length_word):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter

    if guess not in chosen_word:
        print(f"You guessed {guess}, that's not in the word. You lose a life.")
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("You lose.")

    print(f"{' '.join(display)}")

    if '_' not in display:
        end_of_game = True
        print("You win.")

    print(stages[lives])