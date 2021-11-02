'''
String:
-->In Python, string is an immutable sequence data type.
-->It is the sequence of Unicode characters wrapped inside single, double, or triple quotes.

# Ex:
name = "Karthi"  # Its a string with double quotes.
name = 'Karthi'  # Its a string with single quotes.
x = '10'         # We can also store integer value in string.

print("------------CRUD Operations------------")
# CRUD Operations
x = 10     # CREATE    --> Write operation
print(x)   # RETRIEVE  --> Read operation
x = 20     # UPDATE
del x      # DELETE

Sequence Operation of String:
--> indexing
--> slicing
--> adding
--> multiplying
--> checking for membership

In addition, Python has built-in functions for,

6.	len():finding the length of a sequence
7.	max()  : for finding its largest element
8.	min(): for finding its smallest elements.
'''
# Indexing: Accessing Particular value

name = "Karthi"
print("My Name is", name)
print("Third index of my name          :", name[3])

num_str = "1234"
print("The given number is             :", num_str)
print("The 0th Index of given number is:", num_str[2])

# Negative Indexing:
name = "Karthi"
print("My Name is", name)
print("Negative index of my name          :", name[-4])

num_str = "1234"
print("The given number is             :", num_str)
print("Negative index of given number is:", num_str[-1])

# Slicing: Accessing Group of value:

name = "Karthi"
print("My Name is", name[:])
print("The Sequence of given string is     :", name[0:4])

num_str = "12345678"
print("The given number is                 :", num_str[:])  # Empty Slicing is nothing but just copying the value
print("The sequence of given number is    :", num_str[1:5])


name = "Karthi"
print("My Name is", name[:])
print("The Sequence of given string is     :", name[:-3])

num_str = "12345678"
print("The given number is                 :", num_str[:])
print("The sequence of given number is     :", num_str[-6:])

# adding(concatenation):
first_name = "Karthi"
last_name = " Ramesh"

full_name = first_name + last_name
print("Addition of both string is:", full_name)

# addition of number string:

num1 = "1357"
num2 = "2468"
num3 = num1 + num2
print("Addition of the two number string:", num3)

# adding two numbers using string;
num1 = int("1357")
num2 = int("2468")
num3 = num1 + num2
print("Addition of the two number string:", num3)


# Multiplying string:
name = "Karthi "
print("The value of multiplied string is: ", name*4)

# Checking for membership
print("H      : ", 'H' in 'HELLO-PYTHON')
print("L      : ", 'L' in 'HELLO-PYTHON')
print("LL     : ", 'LL' in 'HELLO-PYTHON')
print("PH     : ", 'PH' in 'HELLO-PYTHON')
print("-      : ", '-' in 'HELLO-PYTHON')
print("Space  : ", ' ' in 'HELLO PYTHON')
print("B      : ", 'B' not in 'HELLO PYTHON')
message = 'HELLO-PYTHON'
print('H' in message)
print('L' in message)

# Built in Function:
name = "Karthi"
print("Length of given string is       ,", len(name))
print("Maximum value of given string is,", max(name))
print("Minimum value of given string is,", min(name))