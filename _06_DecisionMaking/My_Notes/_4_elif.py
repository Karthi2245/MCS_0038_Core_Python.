'''
elif:
The elif statement enables us to check multiple conditions and execute
the specific block of statements depending upon the true condition among them.

Syntax:
if expression 1:
    # block of statements

elif expression 2:
    # block of statements

elif expression 3:
    # block of statements

else:
    # block of statements

'''
'''
# Ex:
print("Select your ride:")
print("1  Bike")
print("2. Car")
print("3. SUV")
choice = int(input())
if choice == 1:
    print("You have selected Bike")
elif choice == 2:
    print( "You have selected Car")
elif choice == 3 :
    print("You have selected SUV")

else:
    print("Wrong choice!")
'''

'''
# Ex:2
number = int(input("Enter the number?"))
if number==10:
    print("number is equals to 10")
elif number==50:
    print("number is equal to 50")
elif number==100:
    print("number is equal to 100")
else:
    print("number is not equal to 10, 50 or 100")
'''


'''
# Ex: Mark and Grade System:

marks = int(input("Enter the marks? "))
if marks >= 80:
    print("Congrats ! you scored grade A+...")
elif marks > 60 and marks < 80:
    print("You scored grade A ...")
elif marks >50 and marks <= 60:
    print("You scored grade B ...")
elif marks >= 40 and marks <= 50:
    print("You scored grade C ...")
elif marks >= 35:
    print(" You are Just Pass")
else:
    print("Sorry you are fail ?")'''

'''
# Maximum NUmber :
a, b, c = 10, 20, 30
if a > b and a > c:
    print("The Maximum Number is:", a)
elif b > c:
    print("The Maximum Number is:", b)
else:
    print("The Maximum number is :", c)'''
''''
# .Check whether entered year is leap year or not.
year = int(input("Enter a Year:"))

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










































