'''
setdefault():
-->setdefault() takes a maximum of two parameters
Syntax:
--> dict.setdefault(key, default_value)
--> value of the key if it is in the dictionary
--> None if the key is not in the dictionary and default_value is not specified
--> default_value if key is not in the dictionary and default_value is specified
'''

person = {'name': 'Phill', 'age': 22}
age = person.setdefault('age')
print('person = ', person)
print('Age = '.ljust(40, '.'), ':', age)

person = {'name': 'Phill'}

# key is not in the dictionary
salary = person.setdefault('salary')
print('person = '.ljust(40, '.'), ':', person)
print('salary = '.ljust(40, '.'), ':', salary)

# key is not in the dictionary
# default_value is provided
age = person.setdefault('age', 22)
print('person = '.ljust(40, '.'), ':', person)
print('age = '.ljust(40, '.'), ':', age)