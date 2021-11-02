'''
While Loop:
-->The Python while loop allows a part of the code to be executed until the given condition returns false.
It is also known as a pre-tested loop.

-->When we don't know the number of iterations then the while loop is most effective to use.

-->Syntax:
while expression:
    statements
'''
# Ex:
# Printing a number from 1 to 10
# Just Printing:

num = 1
while num <= 10:
    print(num)

    num += 1

# Giving validation: Negative Numbers should not come:
num = int(input("Enter a number which u want to print it from:"))
while num <= 10:
    if num > 0:  # validation part
        print(num)
        num += 1
    else:
        print("Give us a valid Input")
        break

# Print odd numbers:
num = int(input("Enter a number:"))
a = int(input("Enter your range"))
while num <= a:
    if num % 2 == 1:
        print(num)
    num += 1

# REQ: Print even numbers
num = int(input("Enter a number:"))
a = int(input("Enter your range"))
while num <= a:
    if num % 2 == 0:
        print("Even number between given range:", num)
    num += 1

# REQ: Print numbers divisible  by 5:
num = int(input("Enter a number "))
a = int(input("Enter a range"))
while num <= a:
    if num % 5 == 0:
        print("The number in given range is:", num)
    num += 1

# REQ: Print numbers divisible by 7:
num = int(input("Enter a number "))
a = int(input("Enter a range"))
while num <= a:
    if num % 7 == 0:
        print("The number in given range is:", num)
    num += 1

# REQ: Print the number divisible by 3:

    num = int(input("Enter a number "))
    a = int(input("Enter a range"))
    while num <= a:
        if num % 3 == 0:
            print("The number in given range is:", num)
        num += 1

# REQ Print the numbers divisible by 2:

num = int(input("Enter a number "))
a = int(input("Enter a range"))
while num <= a:
    if num % 2 == 0:
        print("The number in given range is:", num)
    num += 1

# Pattern Program:
n = int(input('Enter number of rows : '))
i = 1
while i <= n:
    j = 1
    while j <= i:
        print("*", end=" ")
        j += 1
    print()
    i += 1
# Inverse pattern program.
rows = int(input("Enter your rows"))
i = 1  # i -> Row
while i <= rows:
    j = rows  # j-->Columns
    while i <= j:
        print("*", end=" ")
        j -= 1
    print()
    i += 1

# To Print a number pattern:
n = int(input('Enter number of rows : '))
k = 1
i = 1
while i <= n:
    j = 1
    while j <= i:
        print("{:3d}".format(k), end=" ")
        j += 1
        k += 1
    print()
    i += 1

str1 = 'abc'
str2 = 'defg'
for i in str1:
    print(i)
for j in str2:
    print(j)




