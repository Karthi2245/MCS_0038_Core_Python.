'''
-->The pop() method removes the item at the given index from the list and returns the removed item.
Syntax:
list.pop(index)

'''
# Ex:
# create a list of prime numbers
prime_numbers = [2, 3, 5, 7]
removed_element = prime_numbers.pop(2)
print('Removed Element      :', removed_element)
print('Updated Prime numbers:', prime_numbers)


# programming languages list
languages = ['Python', 'Java', 'C++', 'French', 'C']
return_value = languages.pop(3)
print('Return Value:', return_value)
print('Updated List:', languages)

# Negative Indices:
languages = ['Python', 'Java', 'C++', 'Ruby', 'C']
print('When index is not passed:')
print('Return Value:', languages.pop())
print('Updated List:', languages)
print('\nWhen -1 is passed:')
print('Return Value:', languages.pop(-1))
print('Updated List:', languages)
print('\nWhen -3 is passed:')
print('Return Value:', languages.pop(-3))
print('Updated List:', languages)