# Battleships
![Battleships game](assets/readme/battleships_game.png)

Link to deployed game is available at - [battleships game](https://battleships-game-2024-1746bf9acf31.herokuapp.com/)
## Introduction
Battle ships is a strategy guessing game, played on a grid that scores players based on how many targets they manage to guess the location of. Typically an online battleships game is played against either a computer or another player, but my version of battleships is played differen in which players are still given points depending on how many targets they hit but they are also given a set amount of lives. If they manage to hit all the targets within the set amount of lives they will win the game but if they don't, they will lose.
## Project
#### The aim of this project is to:
- produce a game that scores players on the targets they hit
- displays messages based on user inputs
- gives the player a set amount of lives and if they don't hit all the targets then ends the game
- displays certain symbols depending on if the player has hit or missed a target
- validates players inputs by cross referencing the inputs to the players grid

### User goals
- get a clear understanding of how the game works
- be able to enter a guess for both the row and column of the target 
- if the guess is invalid then be informed 
- be informed of when the game is over

### Pre Development
Before writing any code for the project I decided to create a flow chart to outline the general direction of the game and the steps necessary.
![flowchat](assets/readme/flowchart.png)
## Features
#### Welcome message 
![Welcome message](assets/readme/Welcome_message.png)
- The welcome message is a brief message explaining the game to the user
- The welcome message also indicates the amount of lives the user has at the start of the game

#### User input (Row)
![User input for row](assets/readme/row_validation.png)
- The user input for row allows users to make their guess for which row the target might be on
- The row guess also comes with a valudation in which uses can't enter an empty space

#### User input (Column)
![User input for column](assets/readme/column_validation.png)
- The user input for column also allows users to enter their guess for which column the target might be on
- Column guess also comes with the same validation as row guess

#### Board display
![Board display](assets/readme/board_display.png)
- The board display shows the players their board at the start of the game
- The board display also shows users that the first row and column is assigned zero rather than one

#### Symbols on board
![Symbols showing on board](assets/readme/symbols_onboard.png)

![hit target](assets/readme/hit_target.png)
- Once the user has made their guess the board will be displayed with markers on it
- Depending on if the users guess was right or wrong will determine what is displayed
- If the user hit a target the board will be displayed with '#' but if they missed the target then the board will be displayed with 'X'

#### Lives counter
![Lives counter](assets/readme/Lives_counter.png)
- The lives counter informs the user of how many lives they have remaining
- The counter is displayed along with the symbols on board messages after the users guess

#### Points counter
![Points counter](assets/readme/points_counter.png)
- The points counter informs the user of how many targets they have hit
- The points counter is displayed along side the lives counter

#### Endgame message
![Endgame message](assets/readme/endgame_message.png)
- The endgame message is a short message indicating that the game has ended
- The game can end by one of the conditions being met either lives reaching zero or points reaching five

#### Congratulations message
![Congratulations message](assets/readme/win_message.png)
- The congratulations message is the condition in which the user wins the game
- This message is displayed if the user sinks all five targets

## Technologies Used
- Python
- Github
- Heroku
- Gitpod
- Node.js

## Testing
Information regarding testing is available on - [Testing page](TESTING.md)

## Deployment
#### The game has been deployed through Github to Heroku
The steps to deploy are:
- Go on the [Heroku website](https://www.heroku.com/home) as sign in (or create an account)
- Click on create app, choose a unique name and select the region you're in
- Go to the settings tab of the app
- Go onto the config settings and add the key PORT with the value of 8000
- In the same tab (settings) select the stacks Python and Node.js
- Go back the deploy tab in the app creation and link the github repository to Heroku
- Select automatic deploys (optional)
- Finally click deploy branch with main as the selected branch (should already be on main)

### Local Deployment
The steps to fork a repository are:
- Log in to Github (if you have an account, if not sign up for github)
- Go to the repository for Wonders Quiz, Regan Boreland/wondersquiz
- Click fork on the right hand side of the screen (located between notifications and star/saved)

The steps to clone are:
- Log in to Github
- Go to the repository for Wonders Quiz, [Regan Boreland/wondersquiz]( Log in to Github
- Go to the repository for Apex MMA, Regan Boreland/wondersquiz
- Click on the code option and select what you would like to clone with, either: HTTPS, SSH or GitHub CLI.
- Open the terminal in your selected code editor and change the current working directory to the location of where you want the cloned directory.
- Type "Git clone" into the terminal and press enter on your keyboard.)
- Click on the code option and select what you would like to clone with, either: HTTPS, SSH or GitHub CLI.

## Credits
- Jubril Akolade
- Knowledge Mavens - [display board function](https://www.youtube.com/watch?v=tF1WRCrd_HQ)
