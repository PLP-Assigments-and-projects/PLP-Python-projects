#Python gives us super cool ways to organize lots of data!

#Lists 📋
#Ordered collections that are mutable (changeable). Great for storing multiple items.

#A list is like a collection of items (e.g., a shopping list)

fruits = ["apple", "banana", "cherry"]

# Accessing elements
print(fruits[0])  # Outputs: apple

# Modifying an element
fruits[1] = "orange"
print(fruits)  # Outputs: ['apple', 'orange', 'cherry']

# Adding an element
fruits.append("grape")
print(fruits)  # Outputs: ['apple', 'orange', 'cherry', 'grape']


# Tuples 🔒
# Similar to lists but immutable (unchangeable).

# Tuples are like lists, but unchangeable. Once created, you can’t modify them.

coordinates = (10, 20)

# Accessing elements
print(coordinates[0])  # Outputs: 10

# Trying to modify a tuple will raise an error:
# coordinates[0] = 5  # Error! Tuples can't be modified.