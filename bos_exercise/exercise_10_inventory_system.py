"""
Exercise 10: Inventory System (Comprehensive)
Topics: All - Functions, Loops, Lists, Dicts, Sets, Lambda, Copy, File, Recursion
"""

import copy

# Sample inventory
inventory = {
    "apple": {"price": 1.50, "stock": 10},
    "banana": {"price": 0.75, "stock": 25},
    "orange": {"price": 2.00, "stock": 5}
}

# TASK 1: Get total stock
def total_stock(inv):
    """Return total of all stock values."""
    pass

print(f"total_stock: {total_stock(inventory)}")  # Expected: 40


# TASK 2: Low stock items
def low_stock(inv, threshold=10):
    """Return list of items with stock <= threshold."""
    pass

print(f"low_stock: {low_stock(inventory)}")


# TASK 3: Sort by price using lambda
def sort_by_price(inv):
    """Return list of (item, price) sorted by price."""
    pass

print(f"sort_by_price: {sort_by_price(inventory)}")


# TASK 4: Apply discount (use deep copy)
def apply_discount(inv, percent):
    """Return new inventory with prices reduced by percent."""
    # Don't modify original!
    pass

discounted = apply_discount(inventory, 10)
print(f"apply_discount 10%: {discounted}")
print(f"original unchanged: {inventory}")


# TASK 5: Save inventory to file
def save_inventory(inv, filename):
    """Save inventory to text file."""
    # Format: item,price,stock per line
    pass

save_inventory(inventory, "inventory.txt")


# TASK 6: Load inventory from file
def load_inventory(filename):
    """Load inventory from text file."""
    pass

print(f"load_inventory: {load_inventory('inventory.txt')}")


# TASK 7: Total value (recursive for nested categories)
def total_value(inv):
    """Return total value (price * stock for each item)."""
    pass

print(f"total_value: {total_value(inventory)}")


# TASK 8: Find item using break
def find_item(inv, name):
    """Find and return item details. Use break when found."""
    pass

print(f"find_item banana: {find_item(inventory, 'banana')}")
