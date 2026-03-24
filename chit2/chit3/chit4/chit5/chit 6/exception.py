# Step 1: Open the file and handle exceptions
try:
    # Open the file in read mode
    file = open("notes.txt", "r")
    
    # Step 2: Read the content
    content = file.read()
    
    # Step 3: Display the content
    print("Contents of the file:")
    print(content)
    
    # Step 4: Close the file
    file.close()

except FileNotFoundError:
    print("Error: The file 'notes.txt' does not exist.")
