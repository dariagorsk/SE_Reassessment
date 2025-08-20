import random

secret_words = ["victory", "kiwi", "chair", "table", "board", "coach", "lamp", "kitchen", "window", "costume"]
guessed_letters = []
attempt = 0
max_attempts = 5

word = random.choice(secret_words)
hidden_word = "_ ".join("_" for ch in word)

while attempt < max_attempts:
    guess = input(f"Welcome to the game \"Hangman\"! Your goal is to discover a secret word or phrase by guessing letters of the alphabet. Enter only one letter at a time. You have only 5 wrong guesses. The secret word: {hidden_word}. Let's start: ").lower()

    if not guess.isalpha() or len(guess) != 1:
    
    if not guess.isalpha() or len(guess) != 1:
        print("Please, enter only 1 letter! Let's try again: ")
    continue

    if guess in guessed_letters:
    print("You already guessed that letter!")
    continue
    guessed_letters.append(guess)

if not guess in word:
    print("Nope! The letter is not in the secret word. Try again: ")
    continue