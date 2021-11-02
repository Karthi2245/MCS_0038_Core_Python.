'''
Types:
--> Function has two types.
--> built in  Function (Ex:print(),id(),type(),int(),float(),str(),boolean()
--> User Defined Functions.

'''
# Ex:
# print()
str1 = "hello world"
print("The string is".ljust(40, '.'),':', str1)

# id():
print("The Given string is".ljust(40, '.'),':', id(str1))

# type():
print("The Given string is".ljust(40, '.'),':', type(str1))

# int():
num = 12.8
print("The converted int is".ljust(40, '.'),':', int(num))

# float():
num = 12
print("The converted float is".ljust(40, '.'),':',float(num))

# str():
num = 12
str1 = str(num)
print("The converted string is".ljust(40, '.'),':',str1, type(str1))

# boolean():
num = 12
bool1 = bool(num)
print("The converted boolean is ".ljust(40, '.'),':', bool1)

# User Defined Functions;

def full_name(fname, lname):
    name = fname + lname
    return name
fullname = full_name("Karthi", " Ramesh")
print("The Fullname of the canditate is ".ljust(40, '.'),':', fullname)

# Printing the numbers from 1 to 100:

def range_num():
    list=[]
    for i in range(1,11):
     m = i
     print("values are:" , m)
     list.append(m)
    return list
flist=range_num()
print("The Range of number is ", flist)

# The biggest number of the list:
num_list = [1 ,10,23,4,8,22,11]
def big_num():
    list1 = max(num_list)
    return  list1
print("The Biggest number is", big_num())

# Using algorithm:
num_list = [1 ,10,23,4,8,22,11]
for i in num_list:
    print(i)
    #all(i)



# Printing Even Numbers:
list1 = []
def even_num():
    for i in range(1,30):
        m = i
        if m % 2 == 0:

            list1.append(m)
    return list1
print("The list of even number is", even_num())

# The Biggest of two Numbers:
def big_num(a, b):
    if a > b:
        return a
    else:
        return b

print('The Maximum of two number is', big_num(20,30))

# The addition of list:
list1 = [1, 2, 3, 4]
def addition():
    sum = 0
    for i in list1:
        sum = sum + i
    return sum
print("Addition", addition())









