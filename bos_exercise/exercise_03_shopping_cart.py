"""
Exercise 3: Shopping Cart
Topics: Sets, Dictionaries, Lambda, Loops
"""

# Sample catalog
catalog = {
    "apple": 1.50,
    "banana": 0.75,
    "orange": 2.00,
    "milk": 3.50
}

# TASK 1: Create empty cart
def create_cart():
    """Return empty dictionary for cart."""
    pass

print(f"create_cart(): {create_cart()}")


# TASK 2: Add item to cart
def add_item(cart, item, qty=1):
    """Add item with quantity to cart. If exists, increase qty."""
    pass

cart = {}
add_item(cart, "apple", 3)
print(f"cart after adding apples: {cart}")


# TASK 3: Get unique items (set operation)
def get_items_set(cart):
    """Return set of item names in cart."""
    pass

print(f"get_items_set(cart): {get_items_set(cart)}")


# TASK 4: Calculate total using loop
def get_total(cart, catalog):
    """Return total price of cart."""
    # Hint: Loop through cart, multiply qty by price from catalog
    pass

cart = {"apple": 2, "milk": 1}
print(f"get_total(cart, catalog): {get_total(cart, catalog)}")  # Expected: 6.50


# TASK 5: Filter items by price using lambda
def filter_cheap(catalog, max_price):
    """Return dict of items with price <= max_price."""
    # Hint: Use filter() with lambda or dict comprehension
    pass

print(f"filter_cheap(catalog, 2): {filter_cheap(catalog, 2)}")


# TASK 6: Sort items by price using lambda
def sort_by_price(catalog):
    """Return list of (item, price) sorted by price."""
    # Hint: Use sorted() with lambda key
    pass

print(f"sort_by_price(catalog): {sort_by_price(catalog)}")
