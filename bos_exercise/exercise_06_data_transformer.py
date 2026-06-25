"""
Exercise 6: Data Transformer
Topics: Deep & Shallow Copy, Lists, Dictionaries, Comprehensions
"""

import copy

# Sample data
employees = [
    {"name": "Alice", "skills": ["Python", "SQL"]},
    {"name": "Bob", "skills": ["Java", "Python"]}
]

# TASK 1: Shallow copy problem demo
def shallow_copy_demo():
    """Show that shallow copy shares nested lists."""
    original = {"name": "Test", "scores": [1, 2, 3]}
    shallow = copy.copy(original)
    shallow["scores"].append(4)  # This affects original too!
    return original, shallow

print(f"shallow_copy_demo(): {shallow_copy_demo()}")


# TASK 2: Safe copy with deep copy
def safe_copy(data):
    """Return a deep copy of data."""
    pass

original = {"name": "Test", "items": [1, 2]}
copied = safe_copy(original)
print(f"safe_copy result: {copied}")


# TASK 3: Add skill without modifying original
def add_skill(employees, name, skill):
    """Return new list with skill added to employee. Don't modify original."""
    # Hint: Deep copy first, then modify
    pass

result = add_skill(employees, "Alice", "JavaScript")
print(f"add_skill result: {result}")
print(f"original unchanged: {employees}")


# TASK 4: Filter employees by skill
def filter_by_skill(employees, skill):
    """Return employees who have the skill."""
    # Hint: Use list comprehension
    pass

print(f"filter_by_skill(employees, 'Python'): {filter_by_skill(employees, 'Python')}")


# TASK 5: Get all unique skills
def all_skills(employees):
    """Return set of all unique skills."""
    # Hint: Use set comprehension with nested loop
    pass

print(f"all_skills(employees): {all_skills(employees)}")
