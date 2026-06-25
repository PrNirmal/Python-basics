"""
Exercise 1: Fibonacci Calculator
Topics: Functions, Recursion, Loops
"""

# TASK 1: Recursive Fibonacci
def fibonacci_recursive(n):
    """Return nth Fibonacci number using recursion."""
    # Hint: Base cases are n=0 returns 0, n=1 returns 1
    # Recursive: fib(n) = fib(n-1) + fib(n-2)
    pass

print(f"fibonacci_recursive(6): {fibonacci_recursive(6)}")  # Expected: 8


# TASK 2: Fibonacci with FOR loop
def fibonacci_for(n):
    """Return nth Fibonacci number using for loop."""
    # Hint: Start with a=0, b=1, then swap values n times
    pass

print(f"fibonacci_for(6): {fibonacci_for(6)}")  # Expected: 8


# TASK 3: Fibonacci with WHILE loop
def fibonacci_while(n):
    """Return nth Fibonacci number using while loop."""
    # Hint: Use counter variable, loop while counter < n
    pass

print(f"fibonacci_while(6): {fibonacci_while(6)}")  # Expected: 8


# TASK 4: Generate Fibonacci list
def fibonacci_list(n):
    """Return list of first n Fibonacci numbers."""
    # Hint: Build a list by appending each number
    pass

print(f"fibonacci_list(8): {fibonacci_list(8)}")  # Expected: [0, 1, 1, 2, 3, 5, 8, 13]



from bos_exercise.sequence_1 import print_list

print_list([1,2,3,4,5])


# from BOS_Worshop.Day4 import printable_func

# printable_func("Nirmal")

# import copy

a="nirmal"
c=a
print(a is c)
print(a)
print(c)
a="ajay"
print(a)
print(c)
c=30
print(c)
# print(a)

a=[1,23,5]
b=a

a.append(45)
print(a)
# b=[2,3,4]
print(b)

a=[1,2,45]
b=a
# a=+10
print(a)
print(b)

import copy
a=[1,2,3,4]
b=copy.copy(a)

a.append(45)
print(a)
print(b)

a=[[1,2],[3,4]]
b=copy.copy(a)
print(b)
a[0].append(25)
print(a)
print(b)


a=[[1,2],[3,4]]
b=copy.deepcopy(a)
print(b)
a[0].append(34)
print(a)
print(b)



a=b
# copy same object but diffrent reference(variable)
# 
# copy.copy() => shallow copy => copy of object but just outer object
# copy.deepcopy() => deep copy => copy of object and all inner objects 