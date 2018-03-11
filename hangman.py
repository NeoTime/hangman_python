# Hangman

# Use a list of few words
# We need random module
import random

# Welcome
def welcomeScreen():
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

        if guess in validLetters:
            guessed = guessed + guess
        else:
            print("Enter a valid letter. ")

            guess = input()

        if guess not in word:
            turns = turns -1
            if turns == 9:
                print (" o")
            if turns == 8:
                print (" o")
                print (" |")
            if turns == 7:
                print ("  o")
                print ("  |")
                print (" | \ ")
            if turns == 6:
                print ("  o")
                print ("  |")
                print (" / ")
            if turns == 5:
                print ("  o")
                print ("  |")
                print (" / \ ")
            if turns == 4:
                print ("  o")
                print ("  |")
                print ("_/ \_ ")
            if turns == 3:
                print ("  o")
                print ("  |-")
                print ("_/ \_ ")
            if turns == 2:
                print ("  o")
                print (" -|-")
                print ("_/ \_ ")
            if turns == 1:
                print ("YOU HAVE FAILED TO GUESS: ", word)
                break

welcomeScreen()
