from time import sleep
from urllib.request import urlopen


# Game message
print ("Welcome to The Hangman game")
player = input("Enter your name please: ")
sleep(2)
print("Welcome" + player + "!" + "Let's start the game")
print("Have fun")
sleep(2)

def hangman():

    """
    Game logic function
    """
    global count
    global display
    global word
    global guessed
    global play_game
    limit = 5
    guess = input("Your selected word is:" + display + "Take a guess:\n")
    guess = guess.strip()
    if len(guess.strip()) == 0 and len(guess) != 1:
        print("Incorrect Input, please use letter instead\n")    
        hangman()
    elif guess in word:
        guessed.append(guess)
        display = ""
        for i in range(len(word)):
            if (word[i] in guessed):
                display += word[i]
            else:
                display += "_"
            display += " "

        if display.replace(" ", "") == word:
            print("Great work, you guessed the word")
            replay()

        hangman()

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

    # Game application will send GET request to the 
    # below random word generator for purpose of 
    # picking a selection of words needed for the game
    data = urlopen("https://random-word-api.herokuapp.com/word?number=1")
    data = data.read().decode('utf-8')
    word = data[2:len(data)-2]
    length = len(word)
    count = 0
    display = '_ ' * length
    guessed = []
    play_game = ""

main()

hangman()
