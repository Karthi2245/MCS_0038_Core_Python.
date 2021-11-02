'''
Index():

The index() method indexes the first occurrence of the specified value.

The index() method raises an exception if the value is not found.

The index() method is almost the same as the index() method, the only difference is that the index() method returns -1
if the value is not found. (See example below).
'''

# EX:

my_text = "This is my own content"
print("Before using index method:", my_text)
print("After using index method :", my_text.index('e'))

my_text = "This is my own content"
print("Before using index method:", my_text)
print("After using index method :", my_text.index(' '))

my_text = "This is my own content"
print("Before using index method:", my_text)
print("After using index method :", my_text.index('my'))

# my_text = "This is my own content"
# print("Before using index method:", my_text)
# print("After using index method :", my_text.index('Z'))  # ValueError: substring not found

my_text = "This is my own content"
print("Before using index method:", my_text)
print("After using index method :", my_text.index(''))



