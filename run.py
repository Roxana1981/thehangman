import json
import urllib
from time import sleep
from typing import Callable
from urllib.request import urlopen
import gspread

# Visual display of the game progress when user misses selections
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
GUESS_LIMIT = len(HANGMAN_STAGES)
# External app for unlimited word selection needed for the game
RANDOM_WORD_API_URL = "https://random-word-api.herokuapp.com/word?number=1"
player_name = ""


# Hangman function
def hangman(guess_count: int, display: str, word: str, guessed: set):
    guess = input(f"Your selected word is: {display} Take a guess:\n")
    guess = guess.strip().lower()

    # User input is validated for blank submissions
    if len(guess) == 0:
        print("Blank input, please select a letter\n")
        hangman(guess_count, display, word, guessed)

    # User input is validated against multiple letters and non alpha characters
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

    else:
        guess_count += 1
        if guess_count == GUESS_LIMIT:
            print(HANGMAN_STAGES[guess_count - 1])
            print("You did not guess it. I am sorry, you lost :(\n")
            print("The correct word is:", word)
            return replay()

        guessed.add(guess)
        print(HANGMAN_STAGES[guess_count - 1])
        print(f"Incorrect selection. {GUESS_LIMIT - guess_count}",
              "selection left\n")
        hangman(guess_count, display, word, guessed)


# Game function to repeat play process
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

    execute_gspread_operation(set_new_last_player_name)
    hangman(
        guess_count=0,
        display='_ ' * len(word),
        word=word,
        guessed=set()
    )


def set_new_last_player_name(worksheet: gspread.Worksheet):
    global player_name
    worksheet.update_acell("A1", player_name)


def print_last_player_name_if_exists(worksheet: gspread.Worksheet):
    last_player_name = worksheet.acell("A1").value
    if last_player_name is not None:
        print("Last player's name:", last_player_name)
    else:
        print("You are the first player!")


def execute_gspread_operation(callback: Callable[[gspread.Worksheet], None]):
    gc = gspread.service_account("service_account.json")
    try:
        worksheet = gc.open("thehangman").get_worksheet(0)

        callback(worksheet)
    except gspread.exceptions.SpreadsheetNotFound:
        print("Google Spreadsheet does not exist")
    except gspread.exceptions.APIError as e:
        print("Google API Error", e)
    except gspread.exceptions.GSpreadException as e:
        print("GSpread Exception", e)
    finally:
        gc.http_client.session.close()


# Main function of the game
def main():
    global player_name

    execute_gspread_operation(print_last_player_name_if_exists)

    # Player name input section
    player_name = input("Enter your name please: ")
    sleep(0.5)

    # Welcome message
    print("Welcome " + player_name + "!" + " Let's start the hangman game")
    sleep(0.5)
    print(f"You have {GUESS_LIMIT} one letter guesses",
          "to find out a random word")
    print("Have fun!")

    initiate_new_game()


if __name__ == '__main__':
    main()
