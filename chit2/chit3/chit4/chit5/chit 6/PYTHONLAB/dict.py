#create and access dictionary elements
print("create ans access dictionary elements")
my_dict = {"name": "Alice", "age": 25 , "city": "New York"}

#accessing elements
print("Access 'name':", my_dict["name"])  
print("Access 'age':", my_dict.get("age"))  

#Update Dictionary
print("Update Dictionary")
my_dict["age"] = 26  
print("Updated 'age' to 26:", my_dict)

my_dict["profession"] = "Engineer"  
print("Added 'profession':", my_dict)

#removing elements
print("removing elements")
removed_value = my_dict.pop("city")
print("Removed 'city': {removed_value}")
print("Dictionary After Removing 'city':", my_dict)

del my_dict["name"]  
print("Dictionary After Deleting 'name':", my_dict)

my_dict.clear() 
print("Dictionary After Clearing All Elements:", my_dict)

# Merging Dictionaries
print("Merging Dictionaries")
dict1 = {"a": 1, "b": 2, "c": 3}
dict2 = {"d": 4, "e": 5}
print("Dictionary 1:", dict1)
print("Dictionary 2:", dict2)

merged_dict = dict1.copy()
merged_dict.update(dict2)
print("Merged Dictionary:", merged_dict)
