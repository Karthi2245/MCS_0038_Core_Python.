'''
Knowing Whether a file exists or not:
--> The os has sub module called 'path' that contains a method isfile().
--> This method can be used to know whether a file that we are opening really
exists or not

if os.path.isfile(filename):
    f = open(filename , 'r')
else:
    print(filename + 'does not exist'

'''
import os, sys
# Ex: To Check the file whether its exist or not
fname = input("Enter a file name:")
if os.path.isfile(fname):
    f = open(fname)
else:
    print(fname + ' does not exist')
    sys.exit()

print("The file Contents are:")
str1 = f.read()
print(str1)

# To Count the number of lines and words and characters in a file.
fname =input("Enter a file name: ")
if os.path.isfile(fname):
    f = open(fname, 'r')
else:
    print(fname + 'does not exist')

count_line = count_word = count_characters = 0
# read line by line from the file
for line in f:
    words = line.split()
    count_line += 1
    count_word += 1
    count_characters += 1

print('No.of lines:', count_line)
print('No.of lines:', count_word)
print('No.of lines:', count_characters)


a = 'hello'
b = 'world'
print(a == True and b == True)
