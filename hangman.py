# Hangman

# Use a list of few words
# We need random module
import random

# Welcome
def welcomeScreen();
    #Let user type name
    name = input("Enter Your Name: ")
    #WELCOME THE USER
    print ("WELCOME", name, "To a simple hangman game")
    print ("Try to guess the word in 10 tries or less")
    #CALL THE MAIN-FUNCTION
    hangman ()
    print () #PRINT A BLANK ROW

#START OF MAIN PROGRAM
def hangman():
    #HERE WE HAVE LIST OF WORDS
    #RANDOM.CHOICE
    word = random.choice(["saab", "volvo", "toyota", "jeep"])

    #ONLY CHOOSE THE ALPHABET
    validLetters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

    #USER 10 Guesses
    turns = 10
    guessed = ""  #Letters user guessed

    #MAKE SUFE WE HAVE WORD..
    while len(word) > 0:
        msg = ""
        missed = 0
        for letter in word:
            if letter in guessed:
                msg = msg + letter
            else:
                #
                msg = msg + "-" + " "
                missed += 1
        if msg == word:
            print(msg)
            print("You are correct. The word was: ", word)
            break

        print("Guess the word:", msg)

        guess = input()
