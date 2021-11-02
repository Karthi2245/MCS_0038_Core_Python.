'''
The pop() method returns:
--> If key is found - removed/popped element from the dictionary
--> If key is not found - value specified as the second argument (default)
--> If key is not found and default argument is not specified - KeyError exception is raised

Syntax:
dictionary.pop(key, value)

'''
# Ex:
# Pop an element from the dictionary:
sales = { 'apple': 2, 'orange': 3, 'grapes': 4}
element = sales.pop('apple')
print('The popped element is:'.ljust(40, '.'), ':', element)
print('The dictionary is:'.ljust(40, '.'), ':', sales)

#  Pop an element not present from the dictionary

sales = {'apple': 2, 'orange': 3, 'grapes': 4}
element = sales.pop('guava')
print("Updated dict".ljust(40, '.'), ':', element)  # KeyError: 'guava'

# Pop an element not present from the dictionary, provided a default value:
sales = {'apple': 2, 'orange': 3, 'grapes': 4}
element = sales.pop('guava', 'banana')
print('The popped element is:', element)
print('The dictionary is:', sales)




