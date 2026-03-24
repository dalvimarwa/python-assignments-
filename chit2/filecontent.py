# Opening the file
file = open("data.txt", "r")


# Reading the entire content
content = file.read()

# Displaying content
print("File Content:")
print(content)

# Closing file
file.close()
