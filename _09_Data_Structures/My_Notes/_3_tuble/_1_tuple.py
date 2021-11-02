'''
Tuple:
--> Python tuples are a data structure that store an ordered sequence of values
--> Tuples are immutable.
--> This means you cannot change the values in a tuple.

--> Tuple packing is nothing but creating a tuple without parentheses
--> Tuple unpacking means getting the tuple value out of the parentheses.
-->since tuple is immutable so we cannot add any element but
element of tuple is mutable type then we can change the value of the element
'''

# Creating a Tuple:
# Different types of tuples

# Empty tuple
my_tuple = ()
print("adding a tuple".ljust(40, '.'), ':',my_tuple)

# Tuple having integers
my_tuple = (1, 2, 3)
print("adding a tuple".ljust(40, '.'), ':',my_tuple)

# tuple with mixed datatypes
my_tuple = (1, "Hello", 3.4, {1: 'a', 2: 'b'})
print("adding a tuple".ljust(40, '.'), ':',my_tuple)

# nested tuple
my_tuple = ("mouse", [8, 4, 6], (1, 2, 3))
print("adding a tuple".ljust(40, '.'), ':',my_tuple)

# tuple packing :
my_tuple = 3, 4.6, "dog"  # tuple packing
print("adding a tuple".ljust(40, '.'), ':',my_tuple)

a, b, c = my_tuple   # tuple unpacking
print(a)
print(b)
print(c)

my_tuple = ("adding a tuple".ljust(40, '.'), ':', "hello")  # tuple values should be separated with comma(,)
print(type(my_tuple))  # <class 'str'>

# Creating a tuple having one element
my_tuple = ("hello",)
print("adding a tuple".ljust(40, '.'), ':', type(my_tuple))  # <class 'tuple'>

# Parentheses is optional
my_tuple = "hello",
print("adding a tuple".ljust(40, '.'), ':', type(my_tuple))  # <class 'tuple'>


# Accessing tuple elements using indexing
my_tuple = ('p', 'e', 'r', 'm', 'i', 't')
print("adding a tuple".ljust(40, '.'), ':', my_tuple[0])
print("adding a tuple".ljust(40, '.'), ':', my_tuple[5])
# nested tuple
n_tuple = ("mouse", [8, 4, 6], (1, 2, 3))
# nested index
print("adding a tuple".ljust(40, '.'), ':', n_tuple[0][3])
print(n_tuple[1][1])

# Negative Indexing:
my_tuple = ('p', 'e', 'r', 'm', 'i', 't')
print("adding a tuple".ljust(40, '.'), ':', my_tuple[-1])
print(my_tuple[-6])

# slicing:
my_tuple = ('p', 'r', 'o', 'g',' r', 'a',  'm', 'i', 'z')
print("adding a tuple".ljust(40, '.'), ':',my_tuple[1:4])
print("adding a tuple".ljust(40, '.'), ':',my_tuple[-7:-1])
print("adding a tuple".ljust(40, '.'), ':',my_tuple[7:])
print("adding a tuple".ljust(40, '.'), ':',my_tuple[:])

# Changing a Tuple:
my_tuple = (4, 2, 3, [6, 5])
my_tuple[3][0] = 9
# my_tuple[3][2] = 5  # IndexError: list assignment index out of range
print(my_tuple)
my_tuple = ('p', 'r', 'o', 'g', 'r', 'a', 'm', 'i', 'z')
print("adding a tuple".ljust(40, '.'), ':',my_tuple)

# adding:
num1 = (1, 2, 3)
num2 = (4, 5, 6)
print("adding a tuple".ljust(40, '.'), ':', num1 + num2)

# multiplying
even_numbers = (2, 4, 6, 8)
print("Multiplying the even numbers".ljust(40, '.'), ':', even_numbers * 3)
