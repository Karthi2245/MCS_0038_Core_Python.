'''
Types of Files:
Text Files:
--> Text Files store the date in the form of Characters.
ex: "Ganesh" --> Stored as a 6 Characters
Byte Files:
--> Byte Files Store entire data in the form of bytes that is group of 8 bits
each.
ex: A Character is stored as a byte and an integer is stored in the form of
8 bytes.
--> When the data is retrieved from the binary file,the programmer can retrieve
the data as bytes.Binary files can be used to store text, images, audio and
videos.

Opening A file:
--> we should use open() function to open file.This function accepts "filename"
and "open" mode in which to open a file.
ex:
file Handler = open("File name", "open mode", "buffering)

file name = its a name on which data is stored.

open mode = Which represents purpose of opening a file.
--> w = to write a data into a file.
--> r = to read the data from a file.
--> a = to append the data to file.
--> w+ = to write and read data of a file.
--> r+ = to read and write data of a file.
--> a+ = to append and read data of a file.
--> x = to open the file in exclusive creation mode.


buffer = represents a temporary block of memory.Its optional

Close File:
--> A file which is opened should br closed using the "close()"method.
'''
# Reading a File(r): data will be read
f = open("E:\MCS\hello.txt", 'r')
print(f.read())
f.close()

# Write Data(w):  # Data will be overridden
f = open("E:\MCS\hello.txt", 'w')
str1 = f.write("Welcome to the World of Python")
print(str1)
f.close()

# Appending a Data(a): # data will be added to the end
f = open("E:\MCS\hello.txt", 'a')
str1 = f.write("\nI Love Python")
print(str1)
f.close()

# write and read(w+): Existing data will be overridden
f = open("E:\MCS\hello.txt", 'w+')
str1 = f.write("This is the which i want to read")
str2 = f.read()
f.close()

# read and write(r+): Existing data will not be deleted
f = open("E:\MCS\hello.txt", 'r+')
str1 = f.read()
str2 = f.write("\nThis is something i want to add")
print(str2)
f.close()

# to append and read (a+):
# If the file does not exist it will create on its own.
f = open("E:\MCS\hello_python.txt", 'a+')
str1 = f.write("Create a New File")
str2 = f.read()
print(str2)
f.close()

'''
# Open the file in Exclusive mode:
f = open("E:\MCS\hello_world.txt", 'x')
str1 = f.write("Here u can Create ur file exclusively")
str2 = f.read()  # io.UnsupportedOperation: not readable
print(str1)
f.close()     # to close the file.'''






