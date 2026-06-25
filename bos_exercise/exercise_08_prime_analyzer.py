"""
Exercise 8: Prime Number Analyzer
Topics: Loops, Range, Break/Continue/Pass, Nested Loops, Functions
"""

# TASK 1: Check if prime
def is_prime(n):
    """Return True if n is prime, False otherwise."""
    # Hint: Check divisibility from 2 to sqrt(n)
    # Use break when divisor found
    pass

print(f"is_prime(7): {is_prime(7)}")   # Expected: True
print(f"is_prime(10): {is_prime(10)}") # Expected: False


# TASK 2: Find primes in range
def primes_in_range(start, end):
    """Return list of primes between start and end."""
    # Hint: Use is_prime() and continue to skip non-primes
    pass

print(f"primes_in_range(1, 20): {primes_in_range(1, 20)}")


# TASK 3: Count primes up to n
def count_primes(n):
    """Return count of primes from 2 to n."""
    pass

print(f"count_primes(20): {count_primes(20)}")  # Expected: 8


# TASK 4: First n primes
def first_n_primes(n):
    """Return list of first n prime numbers."""
    # Hint: Use while loop until you have n primes
    pass

print(f"first_n_primes(5): {first_n_primes(5)}")  # Expected: [2, 3, 5, 7, 11]


# TASK 5: Prime factors
def prime_factors(n):
    """Return list of prime factors of n."""
    # Example: prime_factors(12) = [2, 2, 3]
    pass

print(f"prime_factors(12): {prime_factors(12)}")  # Expected: [2, 2, 3]
