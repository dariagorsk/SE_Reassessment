import random

secret_words = ["victory", "kiwi", "chair", "table", "board", "coach", "lamp", "kitchen", "window", "costume"]
guessed_letters = []
attempt = 0
max_attempts = 5

word = random.choice(secret_words)
hidden_word = "_ ".join("_" for ch in word)
print(f"Welcome to the game \"Hangman\"! Your goal is to discover a secret word or phrase by guessing letters of the alphabet. Enter only one letter at a time. You have only 5 wrong guesses. The secret word: {hidden_word} ")
