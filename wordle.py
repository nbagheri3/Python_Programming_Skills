# ----------------------------------------------------------------------
# Name:      wordle
# Purpose:   implement the wordle game
# Author(s): Nahal Bagheri and Dasom Lee
# Date:      02/16/2023
# ----------------------------------------------------------------------
"""
Implementation of the wordle game

Prompt a user for the specific file name.
Get a random 5 letter words from the file that user prompts.
Prompt a user for entering a 5 letter word to guess which random letter
is given.
Print the number of user's attempts.
Print color-coded word that user guessed. (RED - not in the
word. YELLOW - in the word but not in the right position, GREEN - in the
word and in the right position.)
Print the appriciate feedbacks if user guessed it right within 6
attempts.
Print an answer if user could not guess it right within 6 attempts.
"""

import string
import random

# Constant assignments
RED = '\033[91m'     # to print text in red: print(RED + text)
GREEN = '\033[92m'   # to print a letter in green: print(GREEN + text)
YELLOW = '\033[93m'  # to print a letter in yellow: print(YELLOW + text)
DEFAULT = '\033[0m'  # to reset the color print(DEFAULT + text)


def choose_wordle(filename):
    """
    Read the file specified and choose a random 5-letter word.
    :param filename: (string) name of the file to choose the wordle from
    :return: (string) the mystery word in uppercase
    """
    with open(filename) as f:
        words = [word.strip(string.punctuation) for line in f for word in
                 line.split()]
        five_letter_words = [word for word in words if
                             len(word) == 5 and word.isalpha()]

    return random.choice(five_letter_words).upper()

def check(wordle, guess):
    """
    Check the player's guess against the wordle and return a string
    representing the color coded feedback for the specified guess.
    Red indicates that the guessed letter is NOT in the word.
    Yellow indicates that the letter is in the word but not in the
    correct spot.
    Green indicates that the letter is in the word in the correct spot.
    :param wordle: (string) the mystery word in upper case
    :param guess: (string) the user's guess in upper case
    :return: (string) a string of red, yellow or green uppercase letters
    """
    # enter your code below and take out the pass statement
    # HINTS: create a working list of letters in the wordle
    # go over the letters in the guess and check for green matches
    # add the green matches to their correct position in an output list
    # remove the green matches from the working list ##############???
    # go over the letters in the guess again
    # compare them to the letters in working list
    # add yellow or red color and add them to their position in output
    # list
    # join the output list into a colored string

    guess = guess.upper()
    wordle = wordle.upper()
    output = [""]*5
    working_list = list(wordle)

    for i in range(len(guess)):
        check = ""
        if guess[i]==wordle[i]:
            check = GREEN + guess[i]
            output[i] = check
            working_list.remove(wordle[i])

    for j in range(len(guess)):
        check = ""
        if guess[j] != wordle[j] and guess[j] in working_list:
            check = YELLOW + guess[j]
            working_list.remove(guess[j])
        else:
            check = RED + guess[j]
        if output[j] == "":
            output[j] = check
    ans = "".join(output)
    return ans

    print(working_list)

def feedback(attempt):
    """
    Print the feedback corresponding to the number of attempts
    it took to guess the wordle.
    :param attempt: (integer) number of attempts needed to guess
    :return: None
    """
    match attempt:
        case 1:
            print("Genius!")
        case 2:
            print("Magnificent!")
        case 3:
            print("Impressive!")
        case 4:
            print("Splendid!")
        case 5:
            print("Great!")
        case 6:
            print("Phew!")


def prompt_guess():
    """
    Prompt the user repeatedly for a valid 5 letter guess that contains
    only letters.  Guess may be in lower or upper case.
    :return: (string) the user's valid guess in upper case
    """
    # user_guess = input("Please enter your 5 letter guess: ")
    # if len(user_guess) == 5 and user_guess.isalpha() :
    # return user_guess.upper()
    #else :

    user_guess = ""
    while (len(user_guess) != 5 or not user_guess.isalpha()):
        user_guess = input(DEFAULT + "Please enter your 5 letter guess: ")

    return user_guess.upper()

def play(wordle):
    """
    Implement the wordle game with all 6 attempts.
    :param wordle: (string) word to be guessed in upper case
    :return: (boolean) True if player guesses within 6 attempts
             False otherwise
    """
    # enter your code below and take out the pass statement
    # call the prompt_guess function to prompt the user for each attempt
    # call the check function to build the colored feedback string
    # call the feedback function to print the final feedback if the user
    # guesses within 6 attempts

    for attempts in range(1,7):
        print(DEFAULT + f'Attempt {attempts}')
        guess = prompt_guess()
        print(check(wordle, guess))

        if guess == wordle:
            feedback(attempts)
            return True
    return False


def main():
    # enter your code following the outline below and take out the
    # pass statement.
    # 1. prompt the player for a filename
    # 2. call choose_wordle and get a random mystery word in uppercase
    #    from the file specified
    # 3. call play to give the user 6 tries
    # 4. if the user has not guessed the wordle, print the correct
    #    answer

    fileName = input("Please enter the filename: ") # 1.
    random_word = choose_wordle(fileName) # 2.
    game = play(random_word) # 3.
    if not game:  #4.
        print(DEFAULT + f'The correct answer is {random_word}')

if __name__ == '__main__':
    main()
