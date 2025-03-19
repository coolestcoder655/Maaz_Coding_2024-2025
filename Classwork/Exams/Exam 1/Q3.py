# You are creating a shopping list for groceries.

# 1. Create a list called `groceries` containing the following items: `"milk"`, `"eggs"`, `"bread"`, `"butter"`.

# 2. Add "cheese" to the list.

# 3. Remove "butter" from the list.

# 4. Print the length of the `groceries` list.

# 5. Print the updated list.

groceries = ["milk", "eggs", "bread", "butter"]

groceries.append("cheese")
groceries.pop(3)
print(len(groceries))
print(groceries)