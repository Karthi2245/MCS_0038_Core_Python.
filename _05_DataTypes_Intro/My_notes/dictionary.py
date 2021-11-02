'''
Dictionary:
->A dictionary is an unordered, changeable, and indexed collection.
->Dictionary stores data in the form of key-value pairs,
 but the key defined for a dictionary needs to be unique.

Methods:
Method	        Description
-> items()	    Returns a new object of the dictionary’s items in (key,value) format.
-> keys()	    Returns a new object of the dictionary’s keys.
-> values()	    Returns a new object of the dictionary’s values.
-> copy()	    Returns a shallow copy of the dictionary.
-> clear()	    Removes all elements from the dictionary.
-> popitem()	Removes and returns an arbitrary item (key,value).

 '''

d = {"car": "Baleno",
     "model": "GT500",
     "year": 2020}
print(d)
print("Specified key:", d['car'])

# Keys cannot be changed.
# You will need to add a new key with the modified value then remove the old one,or create a
# New dict with a dict comprehension.

#Naive method:
# Python code to demonstrate
# changing keys of dictionary
# using naive method

# inititialising dictionary
ini_dict = {'nikhil': 1, 'vashu' : 5,
			'manjeet' : 10, 'akshat' : 15}

# printing initial json
print ("initial 1st dictionary", ini_dict)

# changing keys of dictionary
ini_dict['akash'] = ini_dict['akshat']
del ini_dict['akshat']


# printing final result
print ("final dictionary", str(ini_dict))

# Method  # 2: Using pop()

# Python code to demonstrate
# changing keys of dictionary
# using pop() method

# inititialising dictionary
ini_dict = {'nikhil': 1, 'vashu': 5,
            'manjeet': 10, 'akshat': 15}

# printing initial json
print("initial 1st dictionary", ini_dict)

# changing keys of dictionary
ini_dict['akash'] = ini_dict.pop('akshat')

# printing final result
print("final dictionary", str(ini_dict))

# Method  # 3: Using zip()

# Suppose we want to change all keys of dictionary.

# Python code to demonstrate
# changing all keys of dictionary
# corresponding to list using zip()

# inititialising dictionary
ini_dict = {'nikhil': 1, 'vashu': 5,
            'manjeet': 10, 'akshat': 15}

# initialising list
ini_list = ['a', 'b', 'c', 'd']

# printing initial json
print("initial 1st dictionary", ini_dict)

# changing keys of dictionary
final_dict = dict(zip(ini_list, list(ini_dict.values())))

# printing final result
print("final dictionary", str(final_dict))

