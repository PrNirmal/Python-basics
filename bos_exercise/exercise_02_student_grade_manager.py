"""
Exercise 2: Student Grade Manager
Topics: Lists, Tuples, Dictionaries, Comprehensions
"""

# Sample data
students = [(101, "Alice"), (102, "Bob"), (103, "Charlie")]
grades = {
    101: {"Math": 85, "Science": 90},
    102: {"Math": 72, "Science": 88},
    103: {"Math": 95, "Science": 82}
}

# TASK 1: Create student tuple
def create_student(student_id, name):
    """Return a tuple (student_id, name)."""
    pass

print(f"create_student(104, 'Diana'): {create_student(104, 'Diana')}")


# TASK 2: Get student average
def get_average(grades_dict, student_id):
    """Return average grade for a student."""
    # Hint: Get all grades for student, sum them, divide by count
    pass

print(f"get_average(grades, 101): {get_average(grades, 101)}")  # Expected: 87.5


# TASK 3: Get all students with grade above threshold
def top_students(grades_dict, threshold):
    """Return list of student_ids with average above threshold."""
    # Hint: Use list comprehension
    pass

print(f"top_students(grades, 80): {top_students(grades, 80)}")


# TASK 4: Get all subjects
def get_subjects(grades_dict):
    """Return sorted list of unique subjects."""
    # Hint: Use set comprehension to get unique subjects
    pass

print(f"get_subjects(grades): {get_subjects(grades)}")
