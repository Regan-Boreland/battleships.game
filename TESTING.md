# Testing Battleships
## Manual Testing


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