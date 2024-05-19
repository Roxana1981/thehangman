# Game message
print ("Welcome to The Hangman game")
player = input("Enter your name please: ")
print("Welcome" + player + "!" + "Let's start the game")
print("Have fun")


def hangman():

    """
    Game logic function
    """

    limit = 5
    guess = input("Your selected word is:" + display + "Take a guess:\n")
    guess = guess.strip()
    if len(guess.strip()) == 0 and len(guess) != 1:
        print("Incorrect Input, please use letter instead\n")    
        hangman()
    
    elif guess in word:
        guessed.extend([guess])
        index = word.find(guess)
        word = word[:index]+ "_" + word[index+1:]
        display = display[:index] + guess + display[index+1:]
        print(display+"\n")
    elif guess in guessed:
        print("You have already selected this letter.\n")

    else:
        count+=1

        if count==1:
            print("   _____ \n"
                "  |      \n"
                "  |      \n"
                "  |      \n"
                "  |      \n"
                "  |      \n"
                "  |      \n"
                "__|__\n")
            print("Incorrect selection." + str(limit - count) + "selections left\n")

        elif count == 2:
            print("   _____ \n"
                  "  |     | \n"
                  "  |     |\n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "__|__\n")
            print("Incorrect selection." + str(limit - count) + "selections left\n")
        elif count == 3:
            print("   _____ \n"
                  "  |     | \n"
                  "  |     |\n"
                  "  |     | \n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "__|__\n")
            print("Incorrect selection." + str(limit - count) + "selections left\n")
        elif count == 4:
            print("   _____ \n"
                  "  |     | \n"
                  "  |     |\n"
                  "  |     | \n"
                  "  |     O \n"
                  "  |      \n"
                  "  |      \n"
                  "__|__\n")
            print("Incorrect selection." + str(limit - count) + "selections left\n")
        elif count == 5:
            print("   _____ \n"
                  "  |     | \n"
                  "  |     |\n"
                  "  |     | \n"
                  "  |     O \n"
                  "  |    /|\ \n"
                  "  |    / \ \n"
                  "__|__\n")
            print("You did not guess it. I am sorry, You lost\n")
            print("The correct word is:", word)
            replay()

        if count != limit:
            hangman()


def replay():

    global play_game
    play_game = input("Fancy playing again?Yes=y, No=n\n")
    while play_game not in ["y", "n", "Y", "N"]:
        play_game = input("Fancy playing again?Yes=y, No=n\n")
    if play_game == "y":
        main()
    elif play_game == "n":
        print("Thanks for playing and see you!")
        exit()

def main():
    global count
    global display
    global word
    global guessed
    global length
    global play_game