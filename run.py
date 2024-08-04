import json
import urllib
from time import sleep
from urllib.request import urlopen

HANGMAN_STAGES = [
    "   _____ \n"
    "  |      \n"
    "  |      \n"
    "  |      \n"
    "  |      \n"
    "  |      \n"
    "  |      \n"
    "__|__\n",
    "   _____ \n"
    "  |     | \n"
    "  |     |\n"
    "  |      \n"
    "  |      \n"
    "  |      \n"
    "  |      \n"
    "__|__\n",
    "   _____ \n"
    "  |     | \n"
    "  |     |\n"
    "  |     | \n"
    "  |      \n"
    "  |      \n"
    "  |      \n"
    "__|__\n",
    "   _____ \n"
    "  |     | \n"
    "  |     |\n"
    "  |     | \n"
    "  |     O \n"
    "  |      \n"
    "  |      \n"
    "__|__\n",
    "   _____ \n"
    "  |     |  \n"
    "  |     |  \n"
    "  |     |  \n"
    "  |     O  \n"
    "  |    /|\\ \n"
    "  |    / \\ \n"
    "__|__\n"
]

# Game message
print("Welcome to The Hangman game")
# Player name input section
player = input("Enter your name please: ")
sleep(2)
print("Welcome " + player + "!" + " Let's start the game")
print("Have fun!")
sleep(2)


# Hangman function
def hangman(guess_count: int, display: str, word: str, guessed: set):
    guess = input(f"Your selected word is: {display} Take a guess:\n")
    guess = guess.strip().lower()

    # User input is validated for blank submissions
    if len(guess) == 0:
        print("Blank input, please select a letter\n")
        hangman(guess_count, display, word, guessed)

    # User input is validated against game rules
    elif len(guess) > 1 or not guess.isalpha():
        print("Invalid input, make sure to enter one letter\n")
        hangman(guess_count, display, word, guessed)

    # User input is validated for duplicate letter selection
    elif guess in guessed:
        print("You have already selected this letter.\n")
        hangman(guess_count, display, word, guessed)

    elif guess in word:
        guessed.add(guess)
        new_display = ""

        for i in range(len(word)):
            # Loop for the user section with actual word
            if word[i] in guessed:
                new_display += word[i]
            else:
                new_display += "_"
            new_display += " "

        if new_display.replace(" ", "") == word:
            print("Great work, you guessed the word")
            replay()

        hangman(guess_count, new_display, word, guessed)

    # Visual display of the game progress when user misses selections
    else:
        if guess_count == GUESS_LIMIT:
            print(HANGMAN_STAGES[guess_count - 1])
            print("You did not guess it. I am sorry, you lost :(\n")
            print("The correct word is:", word)
            return replay()

        guess_count += 1
        guessed.add(guess)
        print(HANGMAN_STAGES[guess_count - 1])
        print(f"Incorrect selection. {GUESS_LIMIT - guess_count} selection left\n")
        hangman(guess_count, display, word, guessed)


## Game function to repeat play process
def replay():
    play_game = input("Fancy playing again? Yes=y, No=n\n").lower()

    while play_game not in ["y", "n"]:
        play_game = input("Fancy playing again? Yes=y, No=n\n")

    if play_game == "y":
        initiate_new_game()
    elif play_game == "n":
        print("Thanks for playing and see you!")


def get_random_word() -> str:
    # This function will send GET request to the
    # random word generator API for purpose of
    # picking a selection of words needed for the game
    raw_data = urlopen(RANDOM_WORD_API_URL)
    decoded_data = raw_data.read().decode("utf-8")
    json_data = json.loads(decoded_data)
    word = json_data[0]
    return word.lower()


def initiate_new_game():
    try:
        word = get_random_word()
    except (urllib.error.URLError, urllib.error.HTTPError):
        print("The game is unable to run due to an API failure")
        return

    hangman(
        guess_count=0,
        display='_ ' * len(word),
        word=word,
        guessed=set()
    )


## Main function of the game
def main():
    # Player name input section
    player = input("Enter your name please: ")
    sleep(0.5)

    # Welcome message
    print("Welcome " + player + "!" + " Let's start the hangman game")
    sleep(0.5)
    print(f"You have {GUESS_LIMIT} one letter guesses to find out a random word")
    print("Have fun!")

    initiate_new_game()


if __name__ == '__main__':
    main()
