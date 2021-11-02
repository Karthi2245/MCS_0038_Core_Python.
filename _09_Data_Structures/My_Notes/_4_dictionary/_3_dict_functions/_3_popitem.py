'''
popitem():
-->The Python popitem() method removes and returns the last element (key, value) pair inserted
into the dictionary.
Syntax:
dict.popitem()

--> The popitem() doesn't take any parameters.
--> The popitem() gives error if the key is not exist 
'''
person = {'name': 'Phill', 'age': 22, 'salary': 3500.0}
result = person.popitem()
print('Return Value = '.ljust(40, '.'), ':', result)
print('person = '.ljust(40, '.'), ':', person)
person['profession'] = 'Plumber'
result = person.popitem()
print('Return Value = '.ljust(40, '.'), ':', result)
print('person = '.ljust(40, '.'), ':', person)