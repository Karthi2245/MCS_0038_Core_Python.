'''
Generic Functions:
--> Python have some generic functions:
        --> len()
        --> type()
        --> str()

--> Built-in methods:
    -->
'''

# Ex:

candidate = {'name': 'karthi',
             'file': 'resume',
             'time': 12.45,
             'int_date': 'wednesday'}
print("The given dict".ljust(40, "."), ':', candidate)
print("Length of the dictionary:".ljust(40, "."), ":", len(candidate))
print("type".ljust(40, '.'), ':', type(candidate))
str1 = str(candidate)
print("To convert string".ljust(40, '.'), ':', str1, type(str1))

# To Retrieve all keys from a dictionary:

get_keys = candidate.keys()
get_values = candidate.values()
get_items = candidate.items()
print("Print all the keys".ljust(40, '.'), ':', get_keys)
print("Print all values".ljust(40, '.'), ':', get_values)
print("Print all items".ljust(40, '.'), ':', get_items)  # It gives the items in list format

n1, n2, n3 = (1, 2, 3) # packing

print("unpacking", n1, n2, n3) # unpacking




