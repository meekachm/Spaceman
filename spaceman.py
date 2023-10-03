import random

def load_word():
    '''
    A function that reads a text file of words and randomly selects one to use as the secret word
        from the list.

    Returns: 
           string: The secret word to be used in the spaceman guessing game
    '''
    f = open('words.txt', 'r')
    words_list = f.readlines()
    f.close()
    
    words_list = words_list[0].split(' ') #comment this line out if you use a words.txt file with each word on a new line
    secret_word = random.choice(words_list)
    return secret_word

def is_word_guessed(secret_word, letters_guessed):
    '''
    A function that checks if all the letters of the secret word have been guessed.

    Args:
        secret_word (string): the random word the user is trying to guess.
        letters_guessed (list of strings): list of letters that have been guessed so far.

    Returns: 
        bool: True only if all the letters of secret_word are in letters_guessed, False otherwise
    '''
    # TODO: Loop through the letters in the secret_word and check if a letter is not in lettersGuessed
    # Iterates through each letter
    for letter in secret_word:
        # Check whether letter is in letter_guessed
        if letter not in letters_guessed:
            # If letters have not been guessed, return False
            return False
    # If all letters from secret_word were guessed, return True
    return True

    pass

def get_guessed_word(secret_word, letters_guessed):
    '''
    A function that is used to get a string showing the letters guessed so far in the secret word and underscores for letters that have not been guessed yet.

    Args: 
        secret_word (string): the random word the user is trying to guess.
        letters_guessed (list of strings): list of letters that have been guessed so far.

    Returns: 
        string: letters and underscores.  For letters in the word that the user has guessed correctly, the string should contain the letter at the correct position.  For letters in the word that the user has not yet guessed, shown an _ (underscore) instead.
    '''
    #TODO: Loop through the letters in secret word and build a string that shows the letters that have been guessed correctly so far that are saved in letters_guessed and underscores for the letters that have not been guessed yet
    guessed_word = ""
    # Iterates through each letter
    for letter in secret_word:
        # Check whether letter is in letter_guessed
        if letter in letters_guessed:
            # If letters is guessed, adds the letter to guessed_word
            guessed_word += letter
        else:
            # If letters is not guessed, adds "_"to guessed_word
            guessed_word += "_"
    # Returns updated value to guess_word
    return guessed_word

    pass

def is_guess_in_word(guess, secret_word):
    '''
    A function to check if the guessed letter is in the secret word

    Args:
        guess (string): The letter the player guessed this round
        secret_word (string): The secret word

    Returns:
        bool: True if the guess is in the secret_word, False otherwise

    '''
    #TODO: check if the letter guess is in the secret word
    return guess in secret_word

    pass




def spaceman(secret_word):
    '''
    A function that controls the game of spaceman. Will start spaceman in the command line.

    Args:
      secret_word (string): the secret word to guess.

    '''
    #TODO: show the player information about the game according to the project spec
    print("Welcome to Spaceman!")
    print("The secret word contains: ", len(secret_word), "letters.")
    print("You have 7 incorrect guesses, please enter one letter per round")
    print("-------------------------------------------------------------------------")

    #TODO: Ask the player to guess one letter per round and check that it is only one letter
    letters_guessed = []  # Empty list
    attempts = 7  # Number of attempts allowed

    while attempts > 0:
        guess = input("Enter a letter: ").lower() 
        # validate input is a single alphabetic character
        if len(guess) != 1 or not guess.isalpha():
            print("Please enter one letter at a time.")
            continue
        
        # Check and alert user if they guessed a letter they already guessed
        if guess in letters_guessed:
            print("You already guessed this letter. Try a different one.")
            continue

        # add the guessed letter to letters_guessed
        letters_guessed.append(guess)
        
        #TODO: Check if the guessed letter is in the secret or not and give the player feedback
        #TODO: show the guessed word so far
        if is_guess_in_word(guess, secret_word):
            print("Your guess appears in the word!")
        else:
            print("Sorry your guess was not in the word, try again")
            # decrement by one from the attempts of letter guessed 
            attempts -= 1
            print("You have", attempts, "incorrect guess left.")
        
        # show the current state of the guessed word
        current_state = get_guessed_word(secret_word, letters_guessed)
        print("Guessed word so far:", current_state)
        # display the remaining letters that have not yet been guessed
        remaining_letters = [letter for letter in 'abcdefghijklmnopqrstuvwxyz' if letter not in letters_guessed]
        print("These letters haven't been guessed yet:", ' '.join(remaining_letters))
        print("----------------------------------------------------------------------")

    #TODO: check if the game has been won or lost
        if is_word_guessed(secret_word, letters_guessed):
            print("You won!")
            break

    if attempts == 0:
        print("Sorry you didn't win, try again!")
        print("The word was:", secret_word)
        
    
    # Ask the player if they want to play again
    play_response = input("Would you like to play again? (yes/no): ").lower()
    if play_response == "yes":
        secret_word = load_word()
        spaceman(secret_word)



# function calls to start game
secret_word = load_word()
spaceman(secret_word)
