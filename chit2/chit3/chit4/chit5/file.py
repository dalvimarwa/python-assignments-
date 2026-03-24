# Step 1: Open the file in read mode
try:
    file = open("numbers.txt", "r")
    
    # Step 2: Read the content
    content = file.read()
    
    # Step 3: Split content into numbers (assuming space or newline separated)
    numbers = content.split()  # splits by whitespace
    
    # Step 4: Convert strings to floats
    numbers = [float(num) for num in numbers]
    
    # Step 5: Calculate sum
    total = sum(numbers)
    
    # Step 6: Print the total
    print("The total sum of numbers in the file is:", total)
    
    # Step 7: Close the file
    file.close()

except FileNotFoundError:
    print("The file 'numbers.txt' does not exist.")
except ValueError:
    print("The file contains non-numeric data.")
