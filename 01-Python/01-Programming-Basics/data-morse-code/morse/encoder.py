"""
This module provides functions to encode text into Morse code.

Functions:
- encode(text): Encodes a given text into Morse code, separating words with a pipe (|) and
  letters with a space.
- encode_word(word): Encodes a single word into Morse code, separating letters with a space.
"""

from morse.mapping import MORSE  # Dictionary mapping letters to Morse code

def encode(text):
    """
    Encodes the given text into Morse code.
    Words are separated by a pipe (|) and letters by a space.
    """
    # $CHALLENGIFY_BEGIN
    # Remove punctuation from the text
    words = text.replace(",", "") \
                .replace(".", "") \
                .replace("!", "") \
                .replace("?", "") \
                .replace("'", "") \
                .split()  # Split the text into words

    # Encode each word and join them with a pipe symbol
    return "|".join(encode_word(word) for word in words)
    # $CHALLENGIFY_END


def encode_word(word):
    """
    Encodes a single word into Morse code.
    Letters are separated by a space.
    """
    # $CHALLENGIFY_BEGIN
    # Convert each letter to uppercase, find its Morse code, and join with spaces
    return " ".join(MORSE[letter.upper()] for letter in word)
    # $CHALLENGIFY_END


if __name__ == "__main__":
    # Example usage for one word
    EXAMPLE_TEXT = "abc"
    ENCODED_TEXT = encode_word(EXAMPLE_TEXT)
    print(f"Encoded word '{EXAMPLE_TEXT}' to Morse code: '{ENCODED_TEXT}'")

    # Example usage for a sentence
    EXAMPLE_TEXT = "abc ABC"
    ENCODED_TEXT = encode(EXAMPLE_TEXT)
    print(f"Encoded '{EXAMPLE_TEXT}' to Morse code: '{ENCODED_TEXT}'")
