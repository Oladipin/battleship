# Funtime Battleship

The Funtime Battleship ia a Python terminal based game which runs on Heroku

This games is a very simple version of battleship game of the battleship games. It is a single player game and it is more of less like a guessing game.
It is a 6X6 board game and users will try to guess the location of the randomly generated ships on the hidden board.

[This is the live version of the game](https://funtime-battleship-9fa8148be1aa.herokuapp.com/)

![Display all screen sizes](https://i.stack.imgur.com/1xeu1.png)

## How to play

The Funtime Battleship is a 6x6 board game. it is a very simple and modified version. At the beginning of the game, an hidden board with ships placed on it is generate. The game prompts you to make a guess of a row and column in other to hit the ships on the hidden board. There are 3 hidden ships on the board and the user has 6 tries to try and sunk the ship.

### Features

- Starting board
  - Give a brief welcome to the game and inform the user of the input options expected.
  - It display the player board were row and column guesses will be made
  - it informs the users on marking type that will be on the board after every round depending on the outcome

![Starting board](https://i.stack.imgur.com/LT5zD.png)

- Check the guess row and column and mark it appropraitely on the board.
- Gives a message to the users to inform them of the outcome of each round.
- inform users how many turns they have are left to play

![Score board](https://i.stack.imgur.com/o6Wdi.png)

- input validation and error checking
  - User cannot enter a guess outside the stipulated options
  - User cannot make a guess twice within a round

![Data validaton in check](https://i.stack.imgur.com/FrFqe.png)

- Termination
  - The game ends after stipulated number of rounds.
  - User can restart the program, guesses are not the same though.
  - Provide detailed infomration to know the game has ended and should be restarted.

![Counts and Turns](https://i.stack.imgur.com/81yQd.png)


### Testing
- This project has been tested and sufficiently passed the following:
  - Given invalid input strings when number are expected and vise versa, avoids double entry and out of bound inputs
  - Passed the code through the PEP8 checker and there was no issues
  - Tested in the Horeku terminal

### Bugs
- No bugs

### Validator
- No errors were returned from pep8ci.herokuapp.com


### Deployment

This projectwas deployed using the Code Institute's mock terminal got Heroku.
- Steps for deploment:
-  Clone the repository
- set the buildbacks to Python and NodeJS in that order
- Add port to Config Vars
- Link the Heroku app to the github repository
- Click on manual Deploy



