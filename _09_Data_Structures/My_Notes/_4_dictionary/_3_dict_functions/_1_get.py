'''
Dictionary Methods;
--> The get() method returns the value for the specified key if the key is in the dictionary.
--> get() method takes maximum of two parameters:
--> key - key to be searched in the dictionary
--> value (optional) - Value to be returned if the key is not found. The default value is None.

Syntax:

dict.get(key[, value])
'''
person = {'name': 'Phill', 'age': 22}
print('Name: ', person.get('name'))
print('Age: ', person.get('age'))
# value is not provided so it gives none:
print('Salary: ', person.get('salary'))
# value is provided so it gives the default value.
print('Salary: ', person.get('salary', 0.0))


person = {}
print('Salary: ', person.get('salary'))
# print(person['salary'])  KeyError: 'salary'


