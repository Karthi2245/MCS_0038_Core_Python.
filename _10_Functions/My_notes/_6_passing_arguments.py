'''
Passing agruments:(3 ways)
-->Positional arguments:
    An argument is a variable, value or object passed to a function or method as
input. Positional arguments are arguments that need to be included in the
proper position or order
-->Default arguments:
    Default arguments in Python functions are those arguments that take default
values if no explicit values are passed to these arguments from the function
call.
-->Keyword arguments:
    Keyword arguments (or named arguments) are values that,
when passed into a function, are identifiable by specific parameter names.
'''
print(".....Positional Arguments:".center(50))

# Concatination of string:

def full_name(fname, mname, lname):
    name = fname + mname + lname
    return name
fullname = full_name("Karthi", " keyan", " Rameshbabu")
print("The Fullname of the candidate:", fullname)

# Biggest number among three values:
def big_num(a, b, c):
    if a > b:
        if a > c:
            return a
    elif b > c:
        return b
    else:
        return c
x = big_num(10, 21, 19) # scenario 1
y = big_num(25, 12, 18) # Scenario 2
z = big_num(12, 34, 48) # Scenario 3
print("a is greater than b & c", x)
print("b is greater than a & c", y)
print("c is greater than a & b", z)

print("**Default arguments**".center(50))

# Ex 1:
#def full_name(fname, mname="keyan", lname):
# non-default parameter follows default parameter
def full_name(fname, mname="keyan", lname="rameshbau"):
    name = fname + mname + lname
    return name
fullname = full_name("Karthi")
print("The Fullname of the candidate:", fullname)

# Factorial number:
def fac_num(n = 10):
    factorial=1
    for i in range(1,n + 1):
           factorial = factorial*i
    return factorial
num = fac_num()
print("The factorial value of the given number", num)

# sum of even numbers:
def even_num(st, end=10):
    sum = 0
    for even in range (st, end + 1):
        if even % 2 == 0:
            print(even)
            sum += even
    return  sum
sum_even = even_num(1)
print("The sum of the even numbers", sum_even)

# Key word arguments:

# Employee's Profile:

def profile(empid, empnum, systemno, offnum ):
    print(offnum, systemno, empid, empnum)
emp = profile(empid="MCS_0038", empnum="9786910190",systemno="101",offnum="7904134297")

def order_list(list1):
    list1 = [10, 22, 9, 13, 14, 8]
    list1.sort()
    print(list1)
list2 = order_list(list1=[19, 23, 3, 4, 5])
print(list2)

def profile(empid, empnum, systemno, offnum, empname ):
    print(empname, empid, systemno, empnum, offnum)
emp = profile(empnum="9786910190", systemno="101", empid="MCS-0038",
              offnum="7904134297", empname="Karthi")
