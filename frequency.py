"""Analyzes word frequency in Ulysses by James Joyce"""

import string
import nltk


def get_word_list(file_name):
    """ Reads the specified project Gutenberg book.  Header comments,
    punctuation, and whitespace are stripped away.  The function
    returns a list of the words used in the book as a list.
    All words are converted to lower case.
    """
    # load book from file and tokenize
    book = open(file_name, 'r')
    ulysses = book.read()
    ulysses = ulysses.lower()
    ulysses = nltk.word_tokenize(ulysses)

    # Remove everything before beginning
    for i in range(0, int(len(ulysses)-400)):
        if ulysses[i]+ulysses[i+1]+ulysses[i+2] == "stately,plump":
            ulysses = ulysses[i-1:]

    # Remove exceptions
    exceptions = string.punctuation
    for word in ulysses:
        if word in exceptions:
            ulysses.remove(word)

    return ulysses


def get_top_n_words(text, n):
    """ Takes a list of words as input and returns a list of the n most frequently
    occurring words ordered from most to least frequently occurring.

    word_list: a list of words (assumed to all be in lower case with no
    punctuation
    n: the number of words to return
    returns: a list of n most frequently occurring words ordered from most
    frequently to least frequentlyoccurring
    """
    word_list = get_word_list(text)
    word_dict = dict()
    for word in word_list:
        word_dict[word] = word_dict.get(word, 0) + 1

    top_words = []
    for word, number in word_dict.items():
        top_words.append((number, word))
    top_words.sort(reverse=True)
    return top_words[0:n-1]


if __name__ == "__main__":
    print("Running WordFrequency Toolbox")
    # print(string.punctuation)
    print(get_top_n_words("ulysses.txt", 20))
