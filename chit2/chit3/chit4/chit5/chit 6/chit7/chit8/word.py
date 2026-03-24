# Create a dictionary
my_dict = {
    "apple": "A fruit",
    "car": "A vehicle",
    "python": "A programming language"
}

# Take input from user
word = input("Enter a word to search: ")

# Check if the word exists in the dictionary
if word in my_dict:
    print("The word is present in the dictionary.")
    print("Meaning:", my_dict[word])
else:
    print("The word is NOT present in the dictionary.")
