''' if statement:
The if statement is used to test a particular condition and if the condition is true,
it executes a block of code known as if-block.
The condition of if statement can be any valid logical expression
which can be either evaluated to true or false.

Syntax:
if expression:
    statement
'''

# Ex:
a = 20
b = 20
if a == b:
    print('a and b are equal')
print('If block ended')

num = 5
if num >= 10:
    print("num is greater than 10")
print("if block ended")

num = int(input("enter the number?"))
if num%2 == 0:
    print("Number is even")

a = int(input("Enter a? "))
b = int(input("Enter b? "))
c = int(input("Enter c? "))
if a > b and a > c:
    print("a is largest")
if b > a and b > c:
    print("b is largest")
if c > a and c > b:
    print("c is largest")

d = {"Emp.1": "Karthi", "Emp.2": "Karthick", "Emp.3": "Shiva"}
a = "Emp.4"
if a in d.keys():
    print("True")
else:
   print("False")













