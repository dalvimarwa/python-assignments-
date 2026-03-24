# Program to open a file and handle FileNotFoundError

filename = input("Enter the file name to open: ")

try:
    # Attempt to open the file
    file = open(filename, "r")

    # Read and display contents
    content = file.read()
    print("File contents:\n", content)

    # Close file
    file.close()

except FileNotFoundError:
    print("Error: The file you are trying to open does not exist.")
