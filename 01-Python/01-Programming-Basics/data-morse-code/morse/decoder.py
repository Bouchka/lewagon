# $CHALLENGIFY_BEGIN
"""
This module provides functions to decode Morse code into plain text.

Functions:
- decode(morse_text): Decodes a given Morse code string into plain text, separating words by spaces.
- decode_word(morse_word): Decodes a single Morse code word into plain text.
"""

from morse.mapping import MORSE
from morse.encoder import encode  # Used in the main block for example usage

# Create a reverse dictionary to map Morse code back to letters
# Example: {'...': 'S', '.-': 'A', ...}
MORSE_REVERSE = {value: key for key, value in MORSE.items()}


def decode(morse_text):
    """
    Decodes the given Morse code into plain text.
    Words are separated by a pipe (|) and letters by a space.
    """
    # Split the Morse code into words by pipe (|), decode each word, then join with space
    return " ".join(decode_word(morse_word) for morse_word in morse_text.split("|"))


def decode_word(morse_word):
    """
    Decodes a single Morse code word into plain text.
    Letters are separated by a space.
    """
    # Split Morse letters by space, convert each one to its character, then join
    return "".join(MORSE_REVERSE[morse_letter] for morse_letter in morse_word.split())

# $CHALLENGIFY_END


if __name__ == "__main__":
    # This block runs only if the file is executed directly (e.g. `python file.py`)
    # It does NOT run when the file is imported as a module in another script.
    # Useful for testing or demonstrating how the functions in this file work.
    EXAMPLE = "abc"  # Text to encode and decode
    EXAMPLE_MORSE = encode(EXAMPLE)  # Encode it into Morse
    DECODED_TEXT = decode_word(EXAMPLE_MORSE)  # Decode back the Morse word
    print(f"Encoded word '{EXAMPLE}' into '{EXAMPLE_MORSE}'")
    print(f"    and decoded back into plain text: '{DECODED_TEXT}'")
    # $CHALLENGIFY_END

    # Example usage for one sentence
    # $CHALLENGIFY_BEGIN
    EXAMPLE = "abc ABC"  # A phrase with two words
    EXAMPLE_MORSE = encode(EXAMPLE)  # Encode the full text
    DECODED_TEXT = decode(EXAMPLE_MORSE)  # Decode full Morse back to plain text
    print(f"Encoded word '{EXAMPLE}' into '{EXAMPLE_MORSE}'")
    print(f"    and decoded back into plain text: '{DECODED_TEXT}'")
    # $CHALLENGIFY_END
