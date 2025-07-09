# helpers/__init__.py
import random
import string

def generate_password(size, upper=False):
    """Generate a random lowercase ASCII password of given size"""
    letters = string.ascii_uppercase if upper else string.ascii_lowercase
    breakpoint() # <- That's a BREAKPOINT!
    return ''.join(random.choice(letters) for i in range(size))