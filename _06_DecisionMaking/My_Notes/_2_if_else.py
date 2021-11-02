'''
if-else:
The if-else statement provides an else block combined with the if statement
which is executed in the false case of the condition.

Syntax:
if condition:
    print("true condition")
else:
    print(false condition)
'''
# Ex:
number1 = 20
number2 = 30
if number1 >= number2 :
    print("number 1 is greater than number 2")
else:
    print("number 2 is greater than number 1")

'''if (5>10):
  print(5)
else:
  print(10)
else:
  print("End")'''
# SyntaxError : invalid syntax

# Example 1 : Program to check whether a person is eligible to vote or not

age = int (input("Enter your age? "))
if age >= 18:
    print("You are eligible to vote !!")
else:
    print("Sorry! you have to wait !!")

# Example 2: Program to check whether a number is even or not.

num = int(input("enter the number?"))
if num % 2 == 0:
    print("Number is even...")
else:
    print("Number is odd...")

# If the number is positive, we print an appropriate message

num = 3
if num > 0:
    print(num, "is a positive number.")
print("This is always printed.")

num = -1
if num > 0:
    print(num, "is a positive number.")
print("This is also always printed.")



# Program checks if the number is positive or negative:
# And displays an appropriate message

num = 3

# Try these two variations as well.
# num = -5
# num = 0

if num >= 0:
    print("Positive or Zero")
else:
    print("Negative number")