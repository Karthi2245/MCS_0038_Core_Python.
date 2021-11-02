'''
D Drive
--------
folders    books
                - c
                - python
                - java
           onlinematerial
           movies
                - english
                - hindi
                - telugu
           songs
           scanned copies
           Python



'''
'''
Windows       ==>   Folder       File
Linux         ==>   Directory    File 
P.L Python    ==>   Package      module 

Folder : all sub folders or 
         all files or
         combination of folders and files 
         
Package :   I.  all sub packages or 
           II.  all modules or 
          III.  combination of sub packages and modules 
          Example: 
            _0_maths_basics            : II. Its a package, collection of all modules 
            _00_DataStructures_Programs:  I. all sub packages
            _12_OOPs                   :III. combination of sub packages and modules
    
module : Collection of variables, functions and classes
         .py file is a module 
'''
list1 = list()
num1 = 10
num2 = -20

print(abs(num1), abs(num2))


'''
# include<stdio.h>  <==>  python - from, import    builtins.py- default module available
void main():
    printf()
    scanf()

builtins.py
===============
basics:
------
id() print() input() type()
len() max() min() sorted() sum() range()
help()
enumerate()
filter() map()    reduce() --> functools

abs()    :  To get absolute value 
all()    :
any()
ascii()
bin()
chr()
dir()
divmod()
eval()
exec()
hash()
ord() 
pow()
quit()

oops:
-------
delattr()
getattr()
hasattr()
isinstance() issubclass()
repr()
setattr()
object()
classmethod  staticmethod
classes : int  float bool str list tuple dict set 
super
zip

Exception Handling:
--------------------
BaseException
Exception
All Errors
    ArithmeticError
    AttributeError
    KeyError
    NameError
    TypeError


Iterator : 
-------------
iter() next()  
StopIteration

File Handling:
------------------
open()
enter()
exit()
'''
# from builtins import print, input, len, max, min, print, sorted, sum
print(id(10))
print("----Builtin function calls-----")
val = input("Enter any number")
print(val)
len()
max()
min()
print()
sorted()
sum()




int  # x = 10
float
bool  # istrue = True
list
dict  # dict1 = {}