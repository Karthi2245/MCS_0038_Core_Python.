# Function without parameter with return type:
# The addition of list:
list1 = [1, 2, 3, 4]
def addition():
    sum = 0
    for i in list1:
        sum = sum + i
    return sum
print("Addition".ljust(40, '.'), ':', addition())

print("Printing Even Numbers".center(50))
list1 = []
def even_num():
    for i in range(1,30):
        m = i
        if m % 2 == 0:

            list1.append(m)
    return list1
print("The list of even number is".ljust(40, '.'), ':', even_num())

# function without parameters ,without return type:
print("...sum of even numbers..".center(50))
list1 = [1, 2, 3, 4]
def addition():
    sum = 0
    for i in list1:
        sum = sum + i
        print("The sum of even number is".ljust(40, '.'), ':', sum)
addition()
#print("The even numbers are ".ljust(40, '.'), ':', addition())
# it usually gives none as a result if we are not getting any values as return

# fuction with parameter and without return type
# Ex:1
print("addition of list:".center(50))
def addition(a, b):
    c = a + b
    print("The addition".ljust(40, '.'), ':', c)
addition(2, 4)
# EX: 2
print("Printing odd numbers:".center(50))
def odd_num(st, end):
    for odd in range(st, end):
        if odd % 2 == 1:

            print("The odd numbers are".ljust(40, '.'), ':', odd)
odd_number = odd_num(10,20)
'''print("odd number",odd_number) since print statement taking responsibility
cause the out put is none. '''
# Ex: 3
print("Sum of odd numbers:".center(50))
def odd_num(st, end):
    sum = 0
    for odd in range(st, end):
        if odd % 2 == 1:
            sum += odd
    print("The sum of odd numbers".ljust(40, '.'), ':', sum)
    # TO get the total out put we should use the print() under def.

odd_num(30, 1000)

# function with parameter with return type:

# Factorial of the number:

def fac_num(n):
    factorial=1
    for i in range(1,n + 1):
           factorial = factorial*i
    return factorial
num = fac_num(8)
print("The factorial value of the given number", num)














