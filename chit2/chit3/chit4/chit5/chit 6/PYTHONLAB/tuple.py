# Create and Access
print(" Create and Access Tuple")
my_tuple = (10, 20, 30, 40, 50)
print("Created Tuple:", my_tuple)

# Accessing elements
print("Access Element at Index 2:", my_tuple[2])  
print("Access Elements from Index 1 to 3:", my_tuple[1:4])


# 3.2 Nested Tuple
print(" Nested Tuple")
nested_tuple = (1, 2, (3, 4, 5), 6)
print("Nested Tuple:", nested_tuple)
print("Access Inner Tuple Element (Index 2, Sub-Index 1):", nested_tuple[2][1]) 

#Repetition of Tuple
print(" Repetition of Tuple")
repeated_tuple = my_tuple * 2  
print("Repeated Tuple:", repeated_tuple)

#Concatenation of Tuples
print("Concatenation of Tuples")
tuple1 = (100, 200, 300)
tuple2 = (400, 500, 600)
concatenated_tuple = tuple1 + tuple2  
print("Concatenated Tuple:", concatenated_tuple)