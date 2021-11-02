'''
Python dictionary is an unordered collection of items. Each item of a dictionary has a key/value pair.
--> Immutable: int float bool string tuple
--> Mutable  : list, dict, set
In Dictionary,
    --> Keys are Immutable ;Key should be unique.
    --> Value Can be anything.
    --> Inside Dictionary, we cannot create a mutable data types(list,set,dictionary)
    --> In that case we can create a list contain multiple Dictionaries.


'''
# creating a dictionary:
my_books = {1: 'english', 2: 'maths', 3: 'science', 4: 'social'}
print("My dictionary:", my_books)

# Retrieving Dictionary:
print("The value of the given key            :", my_books[4])
print("The type of the variable is           :", my_books, type(my_books))
print("The address of the given dictionary is:", id(my_books))

# Inside Dictionary, we cannot create a mutable data types(list,set,dictionary)

# my_dict = {'MCS-01': 'Karthick', 'MCS-02': 'Karthi', 'MCS-03': 'Kumar', 'MCS-04': 'Sathish',
# {'emp_id': '01','emp_id: 02'},["address", "personal details"]}  # SyntaxError: invalid syntax

# In that case we can create a list contain multiple Dictionaries:
dict_list = [{1: 'a', 2: 'b', 3: 'c'}, {'MCS-01': 'Karthick', 'MCS-02': 'Karthi', 'MCS-03': 'Kumar'}]
print("Print My list which contain dictionary:", dict_list)

# Accessing dictionary:(
print("First print a index of the list:", dict_list[1])  # 1-Index of the list
print("Now Print the particular value of the dict:", dict_list[1]["MCS-01"])  # Then access the dictionary
# adding dictionary:
dict_list[1]["MCS-04"] = "Siva"
print("update list:", dict_list)


