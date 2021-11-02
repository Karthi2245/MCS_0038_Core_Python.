'''
Requirement based working process:
     1. CRUD :  CREATE RETRIEVE UPDATE DELETE
     2. State (Datatype/structure)
     3. Behavior (Operators, DM, Loops)

List:
-->A list in Python is used to store the sequence of various types of data.
-->Python lists are mutable type its mean we can modify its element after it created.

Properties:
--> List is ordered(Maintain insertion order)
--> The element of the list can access by index
--> The Lists are the mutable types
--> A List can store the various elements.(Homogeneous,Heterogeneous)
--> Follows indexing mechanism while storing the elements.
--> It allows duplicate elements.

'''
# List is ordered(Maintain insertion order):
my_list = [2, 6, 1, 5, 3]
print("List won't change its Insertion order:", my_list)  # unlike "SETS"

# The element of the list can access by index:
my_list = [1, 2, 3, 4, 2, 1]
print("Value of the 3rd Index position of given list:", my_list[3])

# The lists are mutable types:
my_list = ['a', 1, [1, 2, 3], (1, 2, 3)]
my_list[2] = 1
print("Print the values of List:", my_list)

my_list = ['a', 1, [1, 2, 3], (1, 2, 3)]
my_list[2][1] = 1
print("Print the values of list:", my_list)
# since its a list inside list so we can change the values

my_list = ['a', 1, [1, 2, 3], (1, 2, 3)]
# my_list[3][2] = 1
# Since its a tuple inside the list so we cannot change the values.
print("Print the values of list:", my_list)
# TypeError: 'tuple' object does not support item assignment

# Can Store Various Elements:(Homogeneous and Heterogeneous.

my_list = ['a', 1, [1, 2, 3], (1, 2, 3), "Karthi"]
my_list1 = [1, 2, 3, 4, 5]
# can store the same data type elements(homogeneous)
print("Print the values of List:", my_list)
# Can store any type of data (Heterogeneous)

# Duplicate elements:
my_list = [1, 2, 3, 4, 1, 4]
print("Print the value of string:", my_list)
# since its a ordered set it  allows to store the duplicate elements.


# find the largest number in the list:
num_list = [256, 528, 324, 123, 536, 452, 982]
num_list.sort()
print('Sorted list'.ljust(40, '.'), ':', num_list)
print('index', num_list[6])
print('Maximum number of list'.ljust(40, '.'), ':', max(num_list))

# Second Largest word in the list:
num_list = [256, 528, 324, 123, 536, 452, 982]
num_list.sort()
print('Sorted list'.ljust(40, '.'), ':', num_list)
print('Second largest num of the list'.ljust(40, '.'), ':', num_list[5])

'''num_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_list = []
odd_list = []
for num in num_list:
    print(num)
    if num % 2 == 0:
        num_list.append(even_list)
        print("The New Even list".ljust(40, '.'), ':', even_list)

    else:
        odd_list.append(num_list)
        print("The New odd list".ljust(40, '.'), ':', odd_list)'''


# list[1,2,3,mcs,4,software, 5,python,6]
# o.p = list = [mcs, software, python,1,2,3,4,5,6]

# str1 = "abc"
#str2 = 'defg'
# o.p = adbecfg

# str1="karnataka"
# print all the repeated characters and count occurrences of that character.

list2 = []
list3 = []
list1 = [1,2,3,'MCS',4,"software", 5,"python",6]
for i in list1:
    if  type(i) == str:
        list2.append(i)

    else:
        type(i) == int
        list3.append(i)

list4 = list2 + list3
print("The new list is", list4)

str1 = 'abc'
str2 = 'defg'
new_str1 = str1[0] + str2[0]
new_str2 = str1[1] + str2[1]
new_str3 = str1[2] + str2[2]
new_str4 = str2[3]
new_str5 = new_str1 + new_str2 + new_str3 + new_str4
print(new_str5)

str1= "karnataka"
duplicates = []
for char in str1:
   if str1.count(char) > 1:
        if char not in duplicates:
            duplicates.append(char)
print(*duplicates)
print(str1.count("k"))
print(str1.count('a'))

# min max


