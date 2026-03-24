try:
    file = open("data.txt", "r")
    print("File opened successfully")
except FileNotFoundError:
    print("File not found")
