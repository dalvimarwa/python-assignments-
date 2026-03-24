# Reading a file line by line

try:
    # Step 1: Open the file in read mode
    file = open("notes.txt", "r")

    # Step 2: Read and print each line separately
    print("File contents:")
    for line in file:
        print(line.strip())   # strip() removes extra newline

    # Step 3: Close the file
    file.close()

except FileNotFoundError:
    print("Error: The file 'notes.txt' does not exist.")
