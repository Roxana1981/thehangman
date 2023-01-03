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

def replay():

def main():