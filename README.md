README.md

I built a game called "Hangman", which prompts a user to guess a secret word by entering one letter at a time. 
In my programme the secret word is randomly chosen from the list of 10 words.
There are certain conditions in the game: 
1. with the lower() function i made sure that an input from a user works regardless of the initial case.
2. only 1 letter can be accepted by the game, otherwise a user gets a warning message.
3. a user might enter a letter twice, so they get a warning message, if not - a letter is storred in the guessed_letters list.
4. if a letter is in the secret word, the games goes through the letters in the word, defines its position and rreplacess an underscore with this letter, showing user a hint.
5. if a letter is not in the word, a user loses 1 attempt.
6. the win condition: if a user guesses all the letters within maximum attempts.
7. the losing condition: if no attempts left and the word is not guessed.
