"""
Exercise 7: Task Manager
Topics: File Handling, Context Managers, Dictionaries, Lists
"""

# TASK 1: Write text to file
def write_to_file(filename, text):
    """Write text to file using 'with' statement."""
    # with open(filename, 'w') as f:
    #     f.write(text)
    pass

write_to_file("test.txt", "Hello World")
print("write_to_file completed")


# TASK 2: Read text from file
def read_from_file(filename):
    """Read and return text from file. Return '' if file not found."""
    # Hint: Use try/except for FileNotFoundError
    pass

print(f"read_from_file('test.txt'): {read_from_file('test.txt')}")


# TASK 3: Append to file
def append_to_file(filename, text):
    """Append text to file using 'a' mode."""
    pass

append_to_file("test.txt", "\nNew line")
print(f"After append: {read_from_file('test.txt')}")


# TASK 4: Write list to file (one item per line)
def write_list(filename, items):
    """Write each item on a new line."""
    pass

write_list("items.txt", ["apple", "banana", "cherry"])


# TASK 5: Read file into list
def read_list(filename):
    """Read file and return list of lines."""
    pass

print(f"read_list('items.txt'): {read_list('items.txt')}")


# TASK 6: Simple context manager class
class FileOpener:
    """Context manager for opening files."""
    def __init__(self, filename, mode='r'):
        self.filename = filename
        self.mode = mode
        self.file = None
    
    def __enter__(self):
        # Open file and return it
        pass
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        # Close file
        pass

# Test context manager
print("Testing FileOpener:")
with FileOpener("test.txt", "r") as f:
    if f:
        print(f"Read via context manager: {f.read()}")
