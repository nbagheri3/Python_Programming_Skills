# ----------------------------------------------------------------------
# Name:      chat
# Purpose:   implement a simple chatbot
# Author(s): Nahal Bagheri and Dasom Lee
# ----------------------------------------------------------------------
"""
This chatbot program talks to the user based on the rules.

The program will first prompt the user for their.
It will keep asking the user to type any messages until the user types
bye.it exits if user types bye or bye with any punctuation (lower,
upper, mix cases)
It will generate a response based on the rules.
It will change the person and print them when the user types (
do/can/will/would) you __? and I (need/think/have/want) ___
"""
import random
import string

# Enter your constant assignments below
SPECIAL_TOPICS = {'family', 'friend', 'friends', 'mom', 'dad','brother',
                  'sister', 'girlfriend','boyfriend', 'children',
                  'son', 'daughter','child', 'wife', 'husband',
                  'home', 'dog', 'cat', 'pet'}
PRONOUNS_MAP = {
    'i': 'you',
    'am': 'are',
    'me': 'you',
    'my': 'your',
    'mine': 'yours',
    'you': 'me',
    'your': 'my',
    'yours': 'mine',
    'he': 'they',
    'she': 'they',
    'him': 'them',
    'her': 'them',
    'they': 'he',
    'them': 'him',
    'their': 'his',
    'theirs': 'his',
}
# Enter the function definition & docstring for the change_person
# function below
# Function to change pronouns in a sentence
def change_person(*words):
    """
    It changes pronouns. It takes as arguments an arbitrary number of
    words,and returns a string obtained by changing the pronouns and
    putting the words together.
    :param *words: arbitrary number of words(list)
    :return: String
    """
    lst = []
    for word in words:
        if word in PRONOUNS_MAP:
            lst.append(PRONOUNS_MAP[word])
        else:
            lst.append(word)
    return ' '.join(lst)

# Enter function definitions & docstrings for any other helper functions


def chat_with(name):
    """
    It keeps asking a user to input until user types bye or bye with my
    punctuation. (lower, upper, mixed cases). It matches the case
    and prints differently based on the rules.
    :param name: string
    :return: Boolean
    """
    request = input('Talk to me please> ')
    words = request.lower().split()
    last_element = words[len(words) - 1]
    last_char = last_element[len(last_element)-1]
    words = [word.strip(string.punctuation) for word in words]

    match words:
        # Rule 1
        case ['bye']:
            return True
        # Rule 2
        case words if any(word in words for word in SPECIAL_TOPICS):
            words_set = set(words)
            found_topics = words_set&SPECIAL_TOPICS
            topic = found_topics.pop()
            print(f'Tell me more about your {topic}, {name}.')
        # Rule 3
        case [('do' | 'can' | 'will' | 'would') as verb, 'you',
                *rest] if last_char == '?':
            list1 = ['No ' + name + ', I ' + verb + ' not ' +
                    change_person(*rest), 'Yes, I ' + verb]
            print(f'{random.choice(list1)}.')
        # Rule 4
        case ['why', *rest] if last_char == '?':
            print('Why not?')
        # Rule 5
        case ['how', *rest] if last_char == '?':
            list2 = ['why do you ask?', 'how would an '
                    'answer to that help you?']
            print(f'{name}, {random.choice(list2)}')
        # Rule 6
        case ['what', *rest] if last_char == '?':
            list3 = ['What do you think', 'Why is that important']
            print(f'{random.choice(list3)} {name}?')
        # Rule 7
        case ['i',('need' | 'think' | 'have' | 'want') as verb,
                *rest]:
            print(f'Why do you {verb} {change_person(*rest)}?')
        # Rule 8
        case ['i', *middle, rest] if 'too' not in rest:
            print(f"I {' '.join(middle)} {rest} too.")
            # Rule 9
        case  [("tell"| "give"| "say") as verb, *rest]:
                print(f"You {verb} {' '.join(rest)}.")

        # Rule 10
        case words if last_char == '?' and not any(word in words
                                                       for word in
                                                       SPECIAL_TOPICS):
            response = random.choice(["I have no clue.", "Maybe."])
            print(response)

        # Rule 11
        case words if "because" in words:
                answer = 'Is that the real reason?'
                print(answer)

        # Rule 12
        case _:
            responses = ["That's interesting.",
                             "Can you elaborate on that?",
                             "That's nice!"]
            print(random.choice(responses))
    return False


def main():
    # Enter your code following the outline below and take out the
    # pass statement.
    # 1.Prompt the user for their name
    # 2.Call chat_with repeatedly passing the name as argument
    # 3.When chat_with returns True, print the goodbye messages.
    user_name = input("Hello. What is your name please? ")
    while not chat_with(user_name):
        pass
    print(f'Bye {user_name}. \nHave a great day!')

if __name__ == '__main__':
    main()