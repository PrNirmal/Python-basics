"""
Exercise 5: Math Operations
Topics: Recursion, Functions, Nested Loops, Range
"""

# TASK 1: Factorial recursive
def factorial_recursive(n):
    """Return n! using recursion."""
    # Base case: 0! = 1
    # Recursive: n! = n * (n-1)!
    pass

print(f"factorial_recursive(5): {factorial_recursive(5)}")  # Expected: 120


# TASK 2: Factorial with loop
def factorial_loop(n):
    """Return n! using for loop."""
    pass

print(f"factorial_loop(5): {factorial_loop(5)}")  # Expected: 120


# TASK 3: Power recursive
def power(base, exp):
    """Return base^exp using recursion."""
    # Base case: exp=0 returns 1
    # Recursive: base^exp = base * base^(exp-1)
    pass

print(f"power(2, 5): {power(2, 5)}")  # Expected: 32


# TASK 4: Sum of digits recursive
def sum_digits(n):
    """Return sum of digits in n."""
    # Hint: n % 10 gives last digit, n // 10 removes it
    pass

print(f"sum_digits(123): {sum_digits(123)}")  # Expected: 6


# TASK 5: Multiplication table (nested loops)
def mult_table(n):
    """Return n x n multiplication table as 2D list."""
    # Hint: Use nested for loops with range
    pass

print(f"mult_table(3): {mult_table(3)}")  # Expected: [[1,2,3],[2,4,6],[3,6,9]]


# TASK 6: Print triangle pattern
def print_triangle(rows):
    """Print right triangle of stars."""
    # Row 1: *
    # Row 2: **
    # Row 3: ***
    pass

print("Triangle (4 rows):")
print_triangle(4)
