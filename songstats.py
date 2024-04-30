# ----------------------------------------------------------------------
# Name:      songstats
# Purpose:   illustrate the use of sets & dictionaries
# Author(s): Nahal Bagheri and Dasom Lee
# Date:      02/22/2023
# ----------------------------------------------------------------------
"""
Enter your docstring with a one-line overview here

and a more detailed description here.
"""
import string


def tally(words):
    """
    Count the words in the word list specified
    :param words: (list of strings) list of lowercase words
    :return: a tally dictionary with items of the form word: count
    """
    words_dict = {words[i]: 0 for i in range(len(words))}

    for word in words:
        words_dict[word] += 1
    return words_dict


def most_common(word_count):
    """
    Print the 8 most common words in the dictionary in descending order
    of frequency, with the number of times they appear.

    :param word_count: dictionary with items of the form letter: count
    :return: None
    """
    print('The 8 most common words are:')
    word_sort = sorted(word_count, key=word_count.get, reverse=True)
    for word in word_sort[:8]:
        print(f'    {word}: appears {word_count[word]} times.')
    return None


def repeats(word_count):
    """
    Print the words (4-letter or longer) that appear more than 3
    times alphabetically.
    :param word_count: dictionary with items of the form letter: count
    :return: None
    """
    print('The following (4-letter or longer) words appear more than 3 '
          'times: ')
    repeated_words = {word for word, count in word_count.items() if
                      len(word) >= 4 and count > 3}
    for word in sorted(repeated_words):
        print(f'    {word}')

# use a set comprehension

def get_words(filename):
    """
    Read the file specified, and return a list of all the words,
    converted to lowercase and stripped of punctuation.
    :param filename: (string) Name of the file containing song lyrics
    :return: (list of strings) list of words in lowercase
    """
    with open(filename) as f:
        words = [word.strip(string.punctuation) for line in f for word in
                 line.split()]
    return [x.lower() for x in words]


def get_stats(words):
    """
    Print the statistics corresponding to the list of words specified.
    :param words: (list of strings) list of lowercase words
    :return: None
    """
    # Call the tally function to build the word count dictionary
    # Then call the appropriate functions and print:
    # 1. The eight most common words in the song in descending order of
    #    frequency, with the number of times they appear.
    # 2. The total number of words in the song.
    # 3. The number of distinct words in the song.
    # 4. The words that are 4-letter or longer and that appear more
    #    than 3 times sorted alphabetically.
    # 5. The longest word.
    tally_word = tally(words)
    most_common(tally_word)
    print(f'There are {len(words)} words in total in the song.')
    print(f'There are {len(tally_word)} distinct words in the song.')
    repeats(tally_word)
    print(f'The longest word in the song is: {max(words, key=len)}.')
    return None


def common_words(words1, words2):
    """
    Print the words (4-letter or longer) that appear in both word lists
    in alphabetical order.
    :param words1: (list of stings)
    :param words2: (list of stings)
    :return: None
    """
    set1 = {word for word in words1 if len(word) >= 4}
    set2 = {word for word in words2 if len(word) >= 4}

    common_set = set1 & set2
    for word in sorted(common_set):
        print(word)
    return None


def main():
    # Hints:
    # Initialize lists to contain the filenames and the word lists
    # Use a loop to prompt the user for the two filenames
    #   and to get the word list corresponding to each file
    # Use a loop to print the statistics corresponding to each song
    # Call common_words to report on the words common to both songs.

    file_name = []
    word_list = []
    flag = 1
    while flag < 3:
        file = input(f"Please enter the filename containing song {flag}: ")
        file_name.append(file)
        flag += 1
        word_list.append(get_words(file))

    for i in range(2):
        print(f'Song Statistics: {file_name[i]}')
        get_stats(word_list[i])
        print('--------------------------------------------------------------'
              '------------------')
    common_words(word_list[0], word_list[1])


if __name__ == '__main__':
    main()