# Define Book class
class Book:
    def __init__(self, title, author, price):
        self.title = title
        self.author = author
        self.price = price

    # Method to display book details
    def display_details(self):
        print(f"Title: {self.title}")
        print(f"Author: {self.author}")
        print(f"Price: ₹{self.price}")
        print("------------------------")

# Create book objects
book1 = Book("Python Programming", "John Doe", 500)
book2 = Book("Data Science Essentials", "Jane Smith", 750)
book3 = Book("Machine Learning", "Alan Turing", 1000)

# Display book details
print("Book Details:")
book1.display_details()
book2.display_details()
book3.display_details()
