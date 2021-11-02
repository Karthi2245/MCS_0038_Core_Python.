'''
Nested if:
Nested if statements is an if statement inside another if statement.

if (expression):
  if(expression):
    Statement of nested if
  else:
    Statement of nested if else
  Statement of outer if
Statement outside if block

'''

'''
if num1 >= num2:
    if num1 == num2:
        print(f'{num1} and {num2} are equal')
    else:
        print(f'{num1} is greater than {num2}')
else:
    print(f'{num1} is smaller than {num2}')'''

'''a = int(input("Enter a number"))
b = int(input("Enter a number"))
if a == b:
    print("a and b are equal")

else:
    if a > b :
        print(" a is greater than b")
    else:

        print(" b is greater than a")'''
'''
year = int(input("Enter a Year"))
if year % 4 == 0:

    if year % 100 == 0:

        if year % 400 == 0:
            print("The given number is Leap Year")
        else:
            print("The Given year is not a leap year")
    else:
        print("The Given year is a Leap year")
else:
    print("The Given Year is not a Leap Year")'''

marks = int(input("Enter Your Mark"))
if marks >= 35:
    print(" Congrats! You are Pass")
    print("1.Continue 2.Discontinue")
    choice = int(input("Enter Your choice:"))
    if choice == 1:
        print("You have choose to Continue")
        a = int(input("Enter Your Preference"))
        if a == 1:
            print("1.HSC ")
            b = int(input("Enter your choice"))
            if b == 1:
                print("You have to I group")
            else:
                print("You have chose to IInd Group")
        else:
            print("2.Diploma")
    else:
        print("You have choose to Discontinue")
else:
    print("Fail")
























