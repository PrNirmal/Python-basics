"""
Exercise 9: Contact Book
Topics: Lambda, Dictionaries, Lists, Tuples, Comprehensions
"""

# Sample contacts
contacts = [
    {"name": "Alice", "phone": "111", "city": "NYC"},
    {"name": "Bob", "phone": "222", "city": "LA"},
    {"name": "Charlie", "phone": "333", "city": "NYC"}
]

# TASK 1: Sort by name using lambda
def sort_by_name(contacts):
    """Return contacts sorted by name."""
    # Hint: sorted(contacts, key=lambda x: x["name"])
    pass

print(f"sort_by_name: {sort_by_name(contacts)}")


# TASK 2: Filter by city using lambda
def filter_by_city(contacts, city):
    """Return contacts in given city."""
    # Hint: Use filter() with lambda
    pass

print(f"filter_by_city NYC: {filter_by_city(contacts, 'NYC')}")


# TASK 3: Get all phone numbers using map
def get_phones(contacts):
    """Return list of phone numbers."""
    # Hint: Use map() with lambda
    pass

print(f"get_phones: {get_phones(contacts)}")


# TASK 4: City count using comprehension
def city_count(contacts):
    """Return dict {city: count}."""
    pass

print(f"city_count: {city_count(contacts)}")


# TASK 5: Contact to tuple
def to_tuple(contact):
    """Convert contact dict to tuple (name, phone, city)."""
    pass

print(f"to_tuple: {to_tuple(contacts[0])}")


# TASK 6: Search contacts
def search(contacts, query):
    """Return contacts where name contains query (case-insensitive)."""
    pass

print(f"search 'li': {search(contacts, 'li')}")
