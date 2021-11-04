from typing import List
import random
def generate_grid() -> List[List[str]]:
    """
    Generates list of lists of letters - i.e. grid for the game.
    e.g. [['I', 'G', 'E'], ['P', 'I', 'S'], ['W', 'M', 'G']]
    """

    grid = [[random.choice(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']).upper() for k in range(3)]for i in range(3)]
    return grid


def get_words(f: str, letters: List[str]) -> List[str]:
    """
    Reads the file f. Checks the words with rules and returns a list of words.
    """
    letters = letters[0] + letters[1] + letters[2]
    
    with open(f, 'r') as file:
        wordlist = [i.lower() for i in file.read().split() if len(i) >= 4 and letters[4].lower() in i]
    
    new_wordlist = []

    for word in  wordlist:
        for letter in word:
            if letter.upper() not in letters:
                break
            if letters.count(letter.upper()) > word.count(letter.lower()):
                break
        else:
            new_wordlist.append(word)
    return new_wordlist


def get_user_words() -> List[str]:
    """
    Gets words from user input and returns a list with these words.
    Usage: enter a word or press ctrl+d to finish.
    """
    try:
        word = input()
        wordlist = [word]
        while word != "":
            user_input = input()
            wordlist.append(user_input)
    except EOFError:
        return wordlist
    return wordlist


def get_pure_user_words(user_words: List[str], letters: List[str], words_from_dict: List[str]) -> List[str]:
    """
    (list, list, list) -> list

    Checks user words with the rules and returns list of those words
    that are not in dictionary.
    """
    pass


def results():
    pass

