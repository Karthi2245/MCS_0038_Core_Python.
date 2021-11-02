'''
String:
->Python string is the collection of the characters surrounded by single quotes, double quotes,
or triple quotes.
->The computer does not understand the characters; internally, it stores manipulated character as
the combination of the 0's and 1's.
->Each character is encoded in the ASCII or Unicode character.
So we can say that Python strings are also called the collection of Unicode characters.
'''
# Creating a string python:
# Using single quotes
str1 = 'Hello Python'
print(str1)
# Using double quotes
str2 = "Hello Python"
print(str2)

# Using triple quotes
str3 = '''''Triple quotes are generally used for  
    represent the multiline or 
    docstring'''
print(str3)
'''
String Indexing:
Like other languages, the indexing of the Python strings starts from 0.

'''
# Ex:
str = "Hello World"
print(str[0])
print(str[1])
print(str[2])
print(str[-3])
print(str[-2])
print(str[-1])

'''
slice operator [] is used to access the individual characters of the string. 
However, we can use the : (colon) operator in Python to access the substring 
from the given string.

'''
# Given String
str = "JAVATPOINT"
# Start Oth index to end
print(str[0:])
# Starts 1th index to 4th index
print(str[1:5])
# Starts 2nd index to 3rd index
print(str[2:4])
# Starts 0th to 2nd index
print(str[:3])
# Starts 4th to 6th index
print(str[4:7])

'''
Reassigning Strings
Updating the content of the strings is as easy as assigning it to a new string. The string object doesn't support item 
assignment i.e., A string can only be replaced with new string since its content cannot be partially replaced. 
Strings are immutable in Python.

'''
# str = "HELLO"
# str[0] = "h"
# print(str)  # str[0] = "h"TypeError: 'str' object does not support item assignment
'''
Deleting String:
Using Del Keyword we can delete the string.
'''
# str1 = "JAVATPOINT"
# del str1
# print(str1)
# NameError: name 'str1' is not defined

str = "Hello"
str1 = " world"
print(str*3) # prints HelloHelloHello
print(str+str1)# prints Hello world
print(str[4]) # prints o
print(str[2:4]); # prints ll
print('w' in str) # prints false as w is not present in str
print('wo' not in str1) # prints false as wo is present in str1.
print(r'C://python37') # prints C://python37 as it is written
print("The string str : %s" % str)  # prints The string str : Hello


# Escape Sequence:
'''If we try print the string which itself has double quotes and single quotes it will leads to syntax
error to overcome from this we would use escape sequence as a solution.'''

# using triple quotes
print('''''They said, "What's there?"''')

# escaping single quotes
print('They said, "What\'s going on?"')

# escaping double quotes
print("They said, \"What's going on?\"")

'''

Sr.         	Escape Sequence	Description	                Example


1.\ newline	       It ignores the new line.                 print("Python1 \
                                                            Python2 \
                                                            Python3")
                                                            Output:Python1 Python2 Python3
2.\\                Backslash	
                                                            print("\\")
                                                            Output:\
3.	\'	            Single Quotes	
                                                            print('\'')
                                                            Output:'
4.	\\''	        Double Quotes	
                                                            print("\"")
                                                            Output:"
                                                                    
5.	\a	            ASCII Bell	                            print("\a")
                                                            
6.	\b	            ASCII Backspace(BS)	                    print("Hello \b World")
                                                            Output:
                                                            Hello World
                                                            
7.	\f	            ASCII Form feed	                        print("Hello \f World!")
                                                            Hello  World!
                                                            
8.	\n	            ASCII Linefeed	                        print("Hello \n World!")
                                                            Output:
                                                            Hello
                                                             World!

9.	\r	            ASCII Carriege Return(CR)	            print("Hello \r World!")
                                                            Output:
                                                            World!
                                                            
10.	\t	            ASCII Horizontal Tab	                print("Hello \t World!")
                                                            Output:
                                                            Hello 	 World!

11.	\v	            ASCII Vertical Tab	                    print("Hello \v World!")
                                                            Output:
                                                            Hello 
                                                             World!
                                                            
12.	\ooo	        Character with octal value	            print("\110\145\154\154\157")
                                                            Output:Hello

13	\ xHH	        Character with hex value.	            print("\x48\x65\x6c\x6c\x6f")
                                                            Output:Hello
                                                            
'''




'''The format()method:
The format() method is the most flexible and useful method in formatting strings.
The curly braces {} are used as the placeholder in the string and replaced by the format() method argument'''


# Using Curly braces
print("{} and {} both are the best friend".format("Devansh", "Abhishek"))

# Positional Argument
print("{1} and {0} best players ".format("Virat", "Rohit"))

# Keyword Argument

'''

Method	                            Description
capitalize()                It capitalizes the first character of the String. This function is deprecated in python3

casefold()                  It returns a version of s suitable for case-less comparisons.

center(width ,fillchar)     It returns a space padded string with the original string centred with equal number of left 
                            and right spaces.
count(string,begin,end)     It counts the number of occurrences of a substring in a String between begin and end index.

decode(encoding = 'UTF8', errors = 'strict')Decodes the string using codec registered for encoding.

encode()                    Encode S using the codec registered for encoding. Default encoding is 'utf-8'.

endswith(suffix ,begin=0,end=len(string))It returns a Boolean value if the string terminates with given suffix between 
                                         begin and end.
                                         
expandtabs(tabsize = 8)     It defines tabs in string to multiple spaces. The default space value is 8.

find(substring ,beginIndex, endIndex)   It returns the index value of the string where substring is found between begin 
                            index and end index.
                            
format(value)               It returns a formatted version of S, using the passed value.

index(subsring, beginIndex, endIndex)It throws an exception if string is not found.  
                                     It works same as find() method.

isalnum()                   It returns true if the characters in the string are alphanumeric i.e., alphabets or numbers 
                            and there is at least 1 character. Otherwise, it returns false.
                        
    
                            
                            
isalpha()                   It returns true if all the characters are alphabets and there is at least one character, 
                            otherwise False.
                            
isdecimal()                 It returns true if all the characters of the string are decimals.

isdigit()                   It returns true if all the characters are digits and there is at least one character,
                            otherwise False.
                            
isidentifier()              It returns true if the string is the valid identifier.

islower()                   It returns true if the characters of a string are in lower case, otherwise false.

isnumeric()                 It returns true if the string contains only numeric characters.

isprintable()               It returns true if all the characters of s are printable or s is empty, false otherwise.

isupper()                   It returns false if characters of a string are in Upper case, otherwise False.

isspace()                   It returns true if the characters of a string are white-space, otherwise false.

istitle()                   It returns true if the string is titled properly and false otherwise. 
                            A title string is the one in which the first character is upper-case 
                            whereas the other characters are lower-case.
                            
isupper()                   It returns true if all the characters of the string(if exists) is true otherwise it 
                            returns false.
                            
join(seq)                   It merges the strings representation of the given sequence.

len(string)	                It returns the length of a string.

ljust(width[,fillchar])     It returns the space padded strings with the original string left justified to the given 
                            width.
                            
lower()                     It converts all the characters of a string to Lower case.

lstrip()                    It removes all leading whitespaces of a string and can also be used to remove particular 
                            character from leading.
                            
partition()                 It searches for the separator sep in S, and returns the part before it, 
                            the separator itself, and the part after it. If the separator is not found, 
                            return S and two empty strings.
                            
maketrans()	                It returns a translation table to be used in translate function.

replace(old,new[,count])    It replaces the old sequence of characters with the new sequence. 
                            The max characters are replaced if max is given.
                            
rfind(str,beg=0,end=len(str))   It is similar to find but it traverses the string in backward direction.

rindex(str,beg=0,end=len(str))It is same as index but it traverses the string in backward direction.

rjust(width,[,fillchar])    Returns a space padded string having original string right justified to 
                            the number of characters specified.
                            
rstrip()                    It removes all trailing whitespace of a string and can also be used to remove particular 
                            character from trailing.
                            
rsplit(sep=None, maxsplit = -1) It is same as split() but it processes the string from the backward direction. 
                                It returns the list of words in the string. 
                                If Separator is not specified then the string splits according to the white-space.
                                
split(str,num=string.count(str)) Splits the string according to the delimiter str. 
                                 The string splits according to the space if the delimiter is not provided. 
                                 It returns the list of substring concatenated with the delimiter.
                                 
splitlines(num=string.count('\n')) It returns the list of strings at each line with newline removed.

startswith(str,beg=0,end=len(str)) It returns a Boolean value if the string starts with given str between begin and end.

strip([chars])	            It is used to perform lstrip() and rstrip() on the string.

swapcase()                  It inverts case of all characters in a string.

title()	                    It is used to convert the string into the title-case i.e., 
                            The string meEruT will be converted to Meerut.
                            
translate(table,deletechars = '') It translates the string according to the translation table passed in the function .

upper()                     It converts all the characters of a string to Upper Case.

zfill(width)                Returns original string leftpadded with zeros to a total of width characters; 
                            intended for numbers, zfill() retains any sign given (less one zero).
                            
rpartition()

'''

