# Game message
print ("Welcome to The Hangman game")
player = input("Enter your name please")
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
        print("Incorrect guess." + str(limit - count) + "guesses left\n")



def replay():

def main():
    count
    display
    word
    guessed