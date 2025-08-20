import random

secret_words = ["victory", "kiwi", "chair", "table", "board", "coach", "lamp", "kitchen", "window", "costume"]
guessed_letters = []
attempt = 0
max_attempts = 5

word = random.choice(secret_words)
hidden_word = ["_" for ch in word]

print(f"Welcome to the game \"Hangman\"! Your goal is to discover a secret word or phrase by guessing letters of the alphabet. Enter only one letter at a time. You have only 5 wrong guesses.") 

while attempt < max_attempts:
    guess = input(f"The secret word: {" ".join(hidden_word)}. Let's start: ").lower()

    if not guess.isalpha() or len(guess) != 1:
        print("Please, enter only 1 letter! Let's try again: ")
        continue

    if guess in guessed_letters:
        print("You already guessed that letter!")
        continue

    guessed_letters.append(guess)

    if guess in word:
        hidden_word = [guess if ch == guess else hidden_word[index] for index, ch in enumerate(word)]
        print("Correct!", " ".join(hidden_word))
    else:
        attempt += 1
        print(f"Nope! The letter is not in the word. Attempts remaining: {max_attempts - attempt}")

    if guessed_letters == word:
        print("Great! You won!")
        break

if attempt >= max_attempts:
    print("Sorry, you lost :(")