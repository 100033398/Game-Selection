# Planning document for Game Selection: 
> By  and  Isaac Gallienne Levi Passanisi 

## Games planned: 
### Higher or Lower game:
- Can have either user guess what number the computer has or the computer guess the number the user is thinking of. 
- Uses input to receive max value for computer guessing. 
- Also uses input for computer guesses either saying “higher”, “lower” or 
“correct” depending on what number the user is thinking of. 
- Uses input for user guesses in order to allow the user to guess numbers, with the program responding “higher” “lower” or “correct”. 

### Rock Paper Scissors:
- This is a rigged game where 1/20 times the user has a chance to win. 
- 19/20 times the program counters perfectly in order to win 
- 1/20 times the program uses the random module in order to pick from a list of 3 things, rock, paper, or scissors. 
- We added this in order to add some interesting luckiness to the game, allowing the user/developer to adjust the probability of the computer winning guaranteed, as if it were an arcade game.

### Blackjack:
- Simple version with 2-11 (2-Ace) 
- The dealer stops if their cards are greater than or equal to 17, but less than 21. 
- The user wins if: 
    - The dealer busts 
    - The user gets a 21 
    - The dealer has less than the user 

- The dealer wins all other times except: 
    - If they draw 

### Hangman:
- The user gets to pick a difficulty level between 1-5, with 5 different words for each level 
- The game automatically fills in all correct letters (as in if there are more than oneoccurrence of the letter) 
- Words can be changed 
- The beginning of each word is capitalized in case the user wants to add sentences. 
- After 10 wrong guesses the user loses. 
- The user can guess the whole word 

### Slot machine:
- Simple game based on a random selection of the options, if the user gets 3 of the same they win 
### Tic-Tac-Toe:
- User plays against random guessing computer 
- User wins if: 
    - User gets 3 in a row 
- Computer wins if:  
    - Computer gets 3 in a row (rare as it randomly places) 

- Tie if: 
    - No one gets 3 in a row 

- Protections: 
    - Only allowed to guess in empty spaces 
    - Only allowed to guess in actual spaces 

### Dice game:
- Simple: 
    - Just roll dice to see who gets more, computer or user. 
### AI trivia:
- Uses AI to ask for question and answers, sending user’s answer back to the AI 

- Protections: 
    - AI told if the user tries to modify AI it will just return ‘incorrect’ 
    - AI told to not listen to anything outside of the system prompt. 
    - Uses .env file in order to not hard code secrets/keys. 

    - AI told to give hard answers 

- Can be customized later to allow user to select difficulty or do short response questions 
### Clock angle calculator 
- Not a game 
- Uses while true: 
    - Makes sure user enters proper integers 
    - Also uses try except to confirm this 
- Does not return wins or add to games played 
- Prints angle between them 
## OTHER FUNCTIONS: 
### print_wins(): 
- Passed user wins in order to be able to give the user updated information on their current 
situation 
- Passed games played to calculate win percentage 
- Passed end_game = True on the end of the game in order to give custom goodbye message 
### is_draw(): 
- Only used in the Tic-Tac-Toe game 
- Used to check if no win conditions met and no more empty spaces left 
- If there are no empty spaces it returns that 

## OTHER INFO: 
- Uses ‘wins’ variable passed and returned in order to keep correct. 
- Tracks games played before entering function in order to stop unnecessary passing/returning of variables 

## MAIN BLOCK: 
- Use a ‘While’ loop so that when the user wants to exit it exits 
- Uses try exception blocks in order to make sure the user entered the right value and to catch any errors 
- If elif else blocks to check for game starts and user selection 
- Set up variables 