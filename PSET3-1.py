import random

WORDLIST_FILENAME = "words.txt"

def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.

    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist

def chooseWord(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

wordlist = loadWords()

def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    isTrue = True
    for letter in secretWord:
        if letter not in lettersGuessed:
            isTrue = False
            break
        else:
            isTrue = True
    return(isTrue)

def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    # FILL IN YOUR CODE HERE...
    guessedWord = secretWord
    for letter in secretWord:
        if letter not in lettersGuessed:
            guessedWord = guessedWord.replace(letter, " _ ")
    return guessedWord


def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    # FILL IN YOUR CODE HERE...
    import string
    alphabet_string = string.ascii_lowercase
    alphabet_list = list(alphabet_string)
    temp_alphabet = alphabet_list[:]

    for letter in alphabet_list:
        if letter in lettersGuessed:
            temp_alphabet.remove(letter)
    return ''.join(map(str, temp_alphabet))

def hangman(secretWord):
    '''
    secretWord: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many
      letters the secretWord contains.

    * Ask the user to supply one guess (i.e. letter) per round.

    * The user should receive feedback immediately after each guess
      about whether their guess appears in the computers word.

    * After each round, you should also display to the user the
      partially guessed word so far, as well as letters that the
      user has not yet guessed.

    Follows the other limitations detailed in the problem write-up.
    '''
    secretLength = len(secretWord)
    guesses = 8
    lettersGuessed = []
    avialableLetters = getAvailableLetters(lettersGuessed)

    print("Welcome to the game, Hangman!")
    print("I am thinking of a word that is " + str(secretLength) + " letters long." )
    print("-------------")

    while guesses > 0:
        print("You have {} guesses left.".format(guesses))
        print("Available letters: {}".format(avialableLetters))

        guess = input("Please guess a letter: ")
        guessLower = str(guess.lower())

        if guess in lettersGuessed:
            print("Oops! You've already guessed that letter: {}".format(getGuessedWord(secretWord, lettersGuessed)))
            print("-------------")

        elif guess in secretWord:
            lettersGuessed.append(guess)
            print("Good guess: {}".format(getGuessedWord(secretWord, lettersGuessed)))
            print("-------------")
            avialableLetters = avialableLetters.replace(guess,'')
            if isWordGuessed(secretWord, lettersGuessed) == True:
                break

        else:
            avialableLetters = avialableLetters.replace(guess,'')
            lettersGuessed.append(guess)
            print("Oops! That letter is not in my word: {}".format(getGuessedWord(secretWord, lettersGuessed)))
            print("-------------")
            guesses -= 1

    if guesses > 0:
        print("Congratulations, you won!")
    else:
        print("Sorry, you ran out of guesses. The word was {}".format(secretWord))


hangman(chooseWord(wordlist))
