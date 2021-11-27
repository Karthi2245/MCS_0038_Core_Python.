'''
--> To store a group of strings into a text file, we have to use the write() method
inside a loop.
'''
'''f = open("E:\MCS\hello_Everyone.txt", 'w')
while str != '@':
    str = input("Enter the data :")
    if str != '@':
        f.write(str+"\n")

f.close()'''

f = open("E:\MCS\hello_Everyone.txt", 'r')
f.readline()  # used to access the line which we want
print(f.readline())
f.close()
# To Read all the content:
f = open("E:\MCS\hello_Everyone.txt", 'r')
str = f.read()
print(str)
f.close()

# Program to append data on existing file and read the content:

f = open("E:\MCS\hello_all.txt", 'a+')

str3 = input("\nEnter a string")
f.write(str3)
f.seek(5, 0)
str3 = f.read()
print(str3)
















