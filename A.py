import random

# List of possible words
words = ['python', 'java', 'hangman', 'programming', 'development', 'code']

def get_random_word():
    return random.choice(words)

def display_word_progress(word, guessed_letters):
    return ' '.join([letter if letter in guessed_letters else '_' for letter in word])

def hangman():
    print("Welcome to Hangman Game!")
    word = get_random_word()
    guessed_letters = set()
    incorrect_guesses = 0
    max_incorrect_guesses = 6

    while incorrect_guesses < max_incorrect_guesses:
        print(f"\nWord: {display_word_progress(word, guessed_letters)}")
        print(f"Incorrect guesses left: {max_incorrect_guesses - incorrect_guesses}")
        
        guess = input("Guess a letter: ").lower()
        
        if len(guess) != 1 or not guess.isalpha():
            print("Please guess a single valid letter.")
            continue
        
        if guess in guessed_letters:
            print(f"You've already guessed '{guess}'!")
        elif guess in word:
            print(f"Good guess! '{guess}' is in the word.")
        else:
            print(f"Sorry, '{guess}' is not in the word.")
            incorrect_guesses += 1

        guessed_letters.add(guess)

        if all(letter in guessed_letters for letter in word):
            print(f"\nCongratulations! You guessed the word: {word}")
            break
    else:
        print(f"\nGame Over! The word was: {word}")

# Run the game
hangman()
