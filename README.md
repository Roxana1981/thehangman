# The Hangman game application
Online word guessing game. Simple and quick.

Please click here [link](https://thehangman.herokuapp.com/) to access the game.

![Main](assets/images/main.png)

## Project background 

The Hangman game was created as part of Milestone project 3. The functionality of the game was developed using Python. The application targets broad population of online users who would like to play a simple game of words guessing, known as The Hangman.

## Application design

-**Overall application concept** - the main concept of the game is for an online user to try to guess randomly selected word. The application logic was developed using Python and includes components such as functions, loop and creation of 
random words with the help of external application connected to this application. The user visualisation of the game progress is based on the basic characters to outline the progress.

-**Player rules** : 
1. Each player has a limit of 5 potential failed attempts to select a correct letter contained in the randomly selected word.
2. If the selected letter is contained in the word, it will be reflected on the screen accordingly.
3. If the selected letter is not contained in the word, the player's 5 attempts continue to reduce and a hangman starts to be displayed on the screen.
4. The outcome of the game is either the player guesses the entire word or the player runs out of the attempts and the game ends with hangman being fully displayed on the screen.

## Application features

## Testing 

## Future application enhancements

**Bugs**

## Deployment process 

The application needed to be deployed to Heroku and the following steps were required to do so:

1. Sign up to Heroku was required.
2. New application needed to be created in Heroku. This required application name to be selected along required region (Europe).
3. Configuration settings were needed to be setup in Heroku such as PORT = 8000.
4. Buildpacks for Python and Nodejs also required to be selected.
5. In the Deploy tab of Heroku GitHub depository needed to be selected in order to connect it with Heroku for deployment.
6. Deploy Branch button in Heroku was used to submit a build of the application in Heroku.
7. When the application was deployed successfully, the URL for the application has become available in the Settings tab in Heroku.

## Credits


