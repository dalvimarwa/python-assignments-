# Step 1: Create a string
my_string = input("Enter a string: ")

# Step 2: Access characters in the string
print("First character:", my_string[0])
print("Last character:", my_string[-1])

# Optional: Access a specific character
index = int(input("Enter an index to access character: "))
if 0 <= index < len(my_string):
    print(f"Character at index {index}:", my_string[index])
else:
    print("Invalid index!")

# Step 3: Find the length of the string
length = len(my_string)
print("Length of the string:", length)
