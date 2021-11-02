'''
remove():
The remove() method removes the first matching element (which is passed as an argument) from the list.

Syntax:
list.remove(element)

-->The remove() method takes a single element as an argument and removes it from the list.
-->If the element doesn't exist, it throws ValueError: list.remove(x): x not in list except


'''

# Ex:
prime_numbers = [2, 3, 5, 7, 9, 11]
prime_numbers.remove(9)
print('Updated List: ', prime_numbers)

animals = ['cat', 'dog', 'rabbit', 'guinea pig']
animals.remove('rabbit')
print('Updated animals list: ', animals)

# list having duplicate value:
animals = ['cat', 'dog', 'dog', 'guinea pig', 'dog']
animals.remove('dog')
print('Updated animals list: ', animals)

# if the value of the list doesn't exist:
animals = ['cat', 'dog', 'rabbit', 'guinea pig']
animals.remove('fish')
print('Updated animals list: ', animals)  # ValueError: list.remove(x): x not in list

