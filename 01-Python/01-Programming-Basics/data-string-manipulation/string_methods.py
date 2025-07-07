# pylint: disable=missing-docstring

def add_comma(a_string):
    """
    returns a copy of the string with every word separated by a comma
    example: add_comma("John Peter Jude") => "John, Peter, Jude"
    """
    # Option 1: Using split + join (BEST)
    return ', '.join(a_string.split())
    # Option 2: Using replace (basic, but not word-aware)
    # return a_string.replace(' ', ', ')

def belongs_to(a_string, a_word):
    """
    returns True if a_string contains a_word
    example: belongs_to("hey jude", "jude") => True
    """
    # Option 1: Using 'in' keyword (BEST)
    return a_word in a_string

def count_repetition(a_string, a_substring):
    """
    returns how many times a_substring occurs in a_string
    example: count_repetition("000123000123", "0") => 6
    """
    # Option 1: Using count() (BEST)
    return a_string.count(a_substring)
    # Option 3: Manual loop (educational, not efficient)
    # return sum(1 for i in range(len(a_string)) if a_string.startswith(a_substring, i))

def is_a_question(a_string):
    """
    returns True if a_string ends with a "?"
    example: is_a_question("How are you?") => True
    """
    # Option 1: Using endswith() (BEST)
    return a_string.endswith('?')
    # Option 2: Check last character
    # return a_string[-1:] == '?'

def remove_surrounding_whitespaces(a_string):
    """
    returns a copy of the string with leading and trailing whitespaces removed
    example: remove_surrounding_whitespaces("  hey yo  ") => "hey yo"
    """
    # Option 1: Using strip() (BEST)
    return a_string.strip()

def replace(initial_string, old_letter, new_letter):
    """
    returns a copy of the string with the new letter replacing the old one
    example: replace("casanova", "a", "o") => "cosonovo"
    """
    # Option 1: Using replace() (BEST)
    return initial_string.replace(old_letter, new_letter)

def full_description_concatenation(first_name, last_name, age):
    """
    returns a sentence with the first_name and the last_name capitalized and
     the age using concatenation
    example: full_description_concatenation("john", "doe", 33) => "John Doe is 33"
    """
    # Option 1: Using + for concatenation (BEST here since required)
    return first_name.capitalize() + ' ' + last_name.capitalize() + ' is ' + str(age)
    # Option 2: Using join with list
    # return ' '.join([first_name.capitalize(), last_name.capitalize()]) + ' is ' + str(age)
    # Option 3: Using string interpolation (f-string)
    # return f"{first_name.capitalize()} {last_name.capitalize()} is {age}"

def full_description_formatting(first_name, last_name, age):
    """
    returns a sentence with the first_name and the last_name capitalized and
     the age using string interpolation
    example: full_description_formatting("john", "doe", 33) => "John Doe is 33"
    """
    # Option 1: Using f-string (BEST)
    return f"{first_name.capitalize()} {last_name.capitalize()} is {age}"
    # Option 2: Using format()
    # return "{} {} is {}".format(first_name.capitalize(), last_name.capitalize(), age)
