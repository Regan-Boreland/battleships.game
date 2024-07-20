# Testing Battleships
## Manual Testing
| **Feature**   | **Action**                    | **Expected Result**          | **Actual Result** |
| ------------- | ----------------------------- | ---------------------------- | ----------------- |
| Welcome message | User is displayed a message explaining the game | Welcome message should be displayed and the players board should be displayed | Works as expected |
| User inputs (row guess and column guess) | Input areas should allow user to enter their selected areas. If the user tries to enter an empty input they should be displayed with a message | Row and column input is displayed and if left empty the user should be displayed with a message | Works as expected |
|Displayed message after entering inputs | User should be displayed with a message depending on if their input hits a target, misses a target or has already been selected | User should be displayed with a message depending on their inputs | Works as expected
| Remaining lives | User should be displayed with remaining lives after their guess | Lives should be displayed in a message once the user has made a guess | Works as expected
| # and X displayed on players board | When the user has made a guess if their guess was correct a # should be displayed on their board and if they were incorrect then an X should be displayed | After the user has made a guess a symbol should be displayed on the board | Works as expected |
| Hit all ships message | When the user has hit all the targets they will be displayed a message indicating the end of the game | User will be displayed a message ending the game | Works as expected
| Used all lives message | User will be displayed a message if they use all their lives without hitting all of the ships | User will be displayed a message | Works as expected |

## Testing Browsers
The Battleships game was tested on the following browsers
- Google Chrome
- Firefox
- Safari

## Validator testing

## Bugs
| **Bug**   | **Solution**                    |
| ------------- | ----------------------------- |
| Points remain at zero even when a target has been hit | Rather than using a separate function to increment the points, I decided to include an if statement in the start_game function incrementing the score if a taget was hit |
| When the project was deployed, the player has no area to enter their row and column guess | This was solved by adding space after the user input|
| When leaving the row/column guess empty and validating the empty input, the user input was displayed again without providing the user with a message | I used a try/except statement and provided the user with a message if the input was entered as empty |
| User can enter the same hit ship coordinates and keep increasing their points | Add an additional if statement informing user that coordinates can't be reused |