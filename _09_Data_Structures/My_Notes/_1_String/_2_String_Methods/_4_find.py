'''
Find():

-->The find() method finds the first occurrence of the specified value.

-->The find() method returns -1 if the value is not found.

-->The find() method is almost the same as the index() method, the only difference is that the index() method raises an exception if the value is not found. (See example below)

Syntax
-->string.find(value, start, end)

'''

# Ex:
my_text = "This is my own content"
print("Before using find method:", my_text)
print("After using find method :", my_text.find('e'))

my_text = "This is my own content"
print("Before using find method:", my_text)
print("After using find method :", my_text.find(' '))

my_text = "This is my own content"
print("Before using find method:", my_text)
print("After using find method :", my_text.find("z"))  # find method at least take one argument to perform.

my_text = "This is my own content"
print("Before using find method:", my_text)
print("After using find method :", my_text.find('my'))  # it takes only first argument.

my_text = "This is my own content"
print("Before using find method:", my_text)
print("After using find method :", my_text.find(''))  # print 0 if we didn't mention anything.

my_text = "This is my own content"
print("Before using find method:", my_text)
print("After using find method :", my_text.find())  # TypeError: find() takes at least 1 argument (0 given)


