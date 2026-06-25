"""
Exercise 4: Password Generator
Topics: Scopes (global, nonlocal), Functions, Range, Break/Continue/Pass
"""

import random
import string

# Global config
DEFAULT_LENGTH = 8

# TASK 1: Read global variable
def get_default_length():
    """Return the DEFAULT_LENGTH value."""
    pass

print(f"get_default_length(): {get_default_length()}")


# TASK 2: Modify global variable
def set_default_length(new_len):
    """Update DEFAULT_LENGTH. Use 'global' keyword."""
    pass

set_default_length(12)
print(f"DEFAULT_LENGTH after update: {DEFAULT_LENGTH}")


# TASK 3: Simple password generator with loop
def generate_password(length=8):
    """Generate random password of given length."""
    # Hint: Use string.ascii_letters + string.digits
    # Loop 'length' times, pick random char each time
    pass

print(f"generate_password(10): {generate_password(10)}")


# TASK 4: Generate password with continue (skip certain chars)
def generate_no_vowels(length=8):
    """Generate password without vowels (a,e,i,o,u)."""
    # Hint: Use while loop, use 'continue' to skip vowels
    pass

print(f"generate_no_vowels(8): {generate_no_vowels(8)}")


# TASK 5: Find valid password using break
def generate_with_digit(max_tries=100):
    """Generate passwords until one has a digit. Use break."""
    # Hint: Generate password, check if it has digit, break if yes
    pass

print(f"generate_with_digit(): {generate_with_digit()}")


# TASK 6: Counter using nonlocal
def create_counter():
    """Return a function that counts how many times it's called."""
    count = 0
    def increment():
        # Use 'nonlocal count' to modify outer variable
        pass
    return increment

counter = create_counter()
counter()
counter()
print(f"counter() called twice, returns: {counter()}")  # Should return 3
