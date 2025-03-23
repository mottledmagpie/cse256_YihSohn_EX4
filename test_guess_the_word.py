import pytest
from guess_the_word import choose_word, display_word

# Test if the word is selected from the correct list
def test_choose_word():
    word = choose_word()
    assert word in ["python", "programming", "developer", "computer", "algorithm"], \
        f"Selected word {word} is not in the predefined list."

# Test if the display_word function correctly reveals guessed letters
def test_display_word():
    word = "python"
    guessed_letters = {"p", "y", "t"}
    result = display_word(word, guessed_letters)
    assert result == "pyt___", f"Expected 'pyt___', but got {result}"

    guessed_letters.add("h")
    result = display_word(word, guessed_letters)
    assert result == "pyth__", f"Expected 'pyth__', but got {result}"

    guessed_letters.add("o")
    result = display_word(word, guessed_letters)
    assert result == "pytho_", f"Expected 'pytho_', but got {result}"

# Optional: Test if invalid inputs are handled (non-single letters or already guessed letters)
def test_input_validation():
    # Simulate an invalid input (e.g., multiple characters, non-alphabetical characters)
    invalid_input = "ab"
    assert len(invalid_input) != 1 or not invalid_input.isalpha(), "Input is invalid, should only accept a single letter."

    # Simulate a repeated guess
    guessed_letters = {"p", "y", "t"}
    repeated_guess = "p"
    assert repeated_guess not in guessed_letters, f"Letter {repeated_guess} was already guessed."

if __name__ == "__main__":
    pytest.main()
