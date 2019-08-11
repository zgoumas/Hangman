secret_word=''
letters_guessed=[]
GLOBAL_ALPHABET = ['a', 'b', 'c', 'd', 'e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
GAME_SCORE = 0


import random
import string

WORDLIST_FILENAME = "words.txt"


def load_words():
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

wordlist = load_words()


def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)
    
    Returns a word from wordlist at random
    """
    return random.choice(wordlist)



def is_word_guessed(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing; assumes all letters are
      lowercase
    letters_guessed: list (of letters), which letters have been guessed so far;
      assumes that all letters are lowercase
    returns: boolean, True if all the letters of secret_word are in letters_guessed;
      False otherwise
    '''
    letters_right = 0
    for char in secret_word:
        if char in letters_guessed:
            letters_right += 1
        else:
            pass
    
    if letters_right == len(secret_word):
        return True
    else:
        return False


def get_guessed_word(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string, comprised of letters, underscores (_), and spaces that represents
      which letters in secret_word have been guessed so far.
    '''
    reveled_letters=""
    for char in secret_word:
        if char in letters_guessed:
            reveled_letters += char
        else:
            reveled_letters += " _ "
    return reveled_letters


def get_available_letters(letters_guessed):
    '''
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string (of letters), comprised of letters that represents which letters have not
      yet been guessed.
    '''
    alphabet = ['a', 'b', 'c', 'd', 'e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    remaining_unguessed_letters = []
    return_string = ""
    
    for char in alphabet:
        if char in letters_guessed:
            pass
        else:
            remaining_unguessed_letters.append(char)
    return_string = ''.join(remaining_unguessed_letters)
    return return_string

      

def hangman(secret_word):
    '''
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    
    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.
      
    * The user should start with 6 guesses

    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    
    * Ask the user to supply one guess per round. Remember to make
      sure that the user puts in a letter!
    
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.
    
    Follows the other limitations detailed in the problem write-up.
    '''
    number_of_guesses = 7  
    warnings = 0
    while number_of_guesses > 0:
        if is_word_guessed(secret_word, letters_guessed) == True:
            break
       
        else:
            print("___________________________________________")
            print("You currently have " + str(number_of_guesses) + " guesses left.")
            print("You currently have " + str(warnings) + " warnings.")
            print("Your avilable letters are: " + get_available_letters(letters_guessed))
            user_guess = input("Enter a letter: ")
            user_guess = user_guess.lower()
            
            if user_guess in letters_guessed: 
                warnings += 1
                print("You already guessed that letter!")
                if warnings >= 3:
                    number_of_guesses -= 1
                else:
                    continue
            
            elif user_guess not in GLOBAL_ALPHABET:
                warnings += 1
                print("Thats not a letter!")
                if warnings >= 3:
                    number_of_guesses -= 1
                else:
                    continue
                
            elif user_guess in secret_word:
                letters_guessed.append(user_guess)
                print("Good guess! The word is: " + get_guessed_word(secret_word, letters_guessed))
                                 
            else:
                letters_guessed.append(user_guess)
                print("Oops! That letter isn't in my word. The word is: " + get_guessed_word(secret_word, letters_guessed))
                number_of_guesses -= 1
   
    if number_of_guesses > 0:
        print("___________________________________________")
        GAME_SCORE = number_of_guesses + len(secret_word)
        return True
    else:
        print("___________________________________________")
        return False


if __name__ == "__main__":
    
    secret_word = choose_word(wordlist)
    if hangman(secret_word) == True:
        print ("Congradulations you won!")
        print ("Your total score is " + str(GAME_SCORE))
    else:
        print("Sorry, you ran out of guesses. The word was " + secret_word +".")
