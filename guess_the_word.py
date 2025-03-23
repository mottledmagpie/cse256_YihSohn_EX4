import random

def choose_word():
    words = ["python", "programming", "developer", "computer", "algorithm"]
    return random.choice(words)

def display_word(word, guessed_letters):
    return "".join(letter if letter in guessed_letters else "_" for letter in word)

def guess_the_word():
    word = choose_word()
    guessed_letters = set()
    attempts = len(word) + 3  # Giving some extra attempts

    print("Welcome to 'Guess the Word'!")
    print("Try to guess the word, one letter at a time.")

    while attempts > 0:
        print("\nWord:", display_word(word, guessed_letters))
        guess = input("Enter a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single valid letter.")
            continue

        if guess in guessed_letters:
            print("You've already guessed that letter.")
            continue

        guessed_letters.add(guess)

        if guess in word:
            print("Good job! That letter is in the word.")
        else:
            print("Incorrect guess.")
            attempts -= 1

        if set(word).issubset(guessed_letters):
            print("\nCongratulations! You guessed the word:", word)
            return

        print(f"Remaining attempts: {attempts}")

    print("\nGame over! The word was:", word)

if __name__ == "__main__":
    guess_the_word()
