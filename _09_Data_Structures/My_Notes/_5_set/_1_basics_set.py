'''
Set:
--> Sets are used to store multiple items in a single variable.
--> A set is a collection which is unordered, unchangeable, and un indexed.
--> Sets are written with curly brackets.({})
--> Elements in the sets are immutable.
--> Set as hole are mutable.
--> Set dose not allow any duplicate elements.
--> Cannot create a ste with mutable objects.

Set Operations:
--> Create
       1. Cannot create a ste with mutable objects.
--> Retrieve
       1. we cannot access individual values in set.
       2. but we can get the individual values by looping.
       3. We can covert the any data structures into set using set() function.

--> Update
       1. As discussed sets as whole is mutable one.so, we can add element into
       the set using add() function:
--> Delete
       1. To remove the set we have to use discard().
       2. To Delete the whole set use del keyword.
--> Union:
       1. Union means adding both sets.
       2. It eliminates the duplicate element of the set and produce the output

'''

# Ex: Create a set:

days = {'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday',
        'sunday'}
print("print the created set".ljust(40, '.'), ':', days)

fruits = {'banana', 'apple', 'mango', 'orange'}
print("the set of fruit is".ljust(40, '.'), ':', fruits)

# num_set = {1, 2, 3, 4, ['a', 'b', 'c']}
# print("the set of numbers is".ljust(40, '.'), ':', num_set)
# TypeError: unhashable type: 'list'

# Retrieve:
days = {'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday',
        'sunday'}
print("print the created set".ljust(40, '.'), ':', days)

for i in days:
    print("Individual values of set".ljust(40, '.'), ':', i)


fruits = ['banana', 'apple', 'mango', 'orange']
set_fruits = set(fruits)
print("the set of fruit is".ljust(40, '.'), ':', set_fruits)
for f in set_fruits:
    print("Individual values of set".ljust(40, '.'), ':', f)

# Update:

days = {'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday'}
print("print the created set".ljust(40, '.'), ':', days)
days.add('sunday')
print("print the created set".ljust(40, '.'), ':', days)

fruits = {'banana', 'apple', 'mango', 'orange'}
print("the set of fruit is".ljust(40, '.'), ':', fruits)
fruits.add('water milan')
print("the set of fruit is".ljust(40, '.'), ':', fruits)


# Delete:

days = {'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday',
        'sunday'}
print("print the created set".ljust(40, '.'), ':', days)
days.discard('wednesday')
print("updates set".ljust(40, '.'), ':', days)

del days
# print("print the created set".ljust(40, '.'), ':', type(days))
# NameError: name 'days' is not defined

# union
days = {'monday', 'tuesday', 'wednesday', 'thursday', 'friday'}
normal_days = {'saturday', 'sunday'}
normal_days = days | normal_days
print("Normal days".ljust(40, '.'), ':', normal_days)

# Intersection:
days = {'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday',
        'sunday'}
week_off = {'saturday', 'sunday'}
week_off = days & week_off
print('week off'.ljust(40, '.'), ':', week_off)

# Difference:

days = {'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday',
        'sunday'}
week_days = {'monday', 'tuesday', 'wednesday', 'thursday', 'friday'}
week_off = days - week_days
print("week off".ljust(40, '.'), ':', week_off)
week_days = days - week_off
#print("week days".ljust(40, '.'), ':', we)


# concatenation:


def full_name(fname,lname):
    name = fname + lname
    return name
s = full_name ("Karthi", "Ramesh")

print(s)

# sum of first 100 even numbers:

# Sum of natural numbers up to num
# Sum of natural numbers up to num

num =0
sum = 0
odd = 0
for num in range(0, 100):
    if num % 2 == 0:
        sum += num
        #num -= 1

    else:
        num % 2 == 1
        odd += num

print("The sum value".ljust(40, '.'), ':', sum)
print("The odd value".ljust(40, '.'), ':', odd)


















