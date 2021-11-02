'''
extend():
-->The extend() method adds the specified list elements (or any iterable) to the end of the current list.
--> Cannot add single element
--> can only iterate iterables.
--> cannot give directly to the print statement.
--> can add any kind of iterables but it will be printed as comma(,) separated values only.
Syntax:
list.extend(iterable)
'''
# Ex:

fruits = ["banana", "orange", "apple", "mango"]
taste = ("spicy", "sweet", "grispy", "weird")
fruits.extend(taste)
print("After using extend method        :", fruits)

num = [1, 2, 3, 4, 5, 6]
letters = ['a', 'b', 'c', 'd', 'e', 'f']
print("The value of the num list is     :", num)
print("The value of the letter list is  :", letters)
num.extend(letters)
print("The Extended list is             :", num)

fruits = ["banana", "orange", "apple", "mango"]
num = 1
fruits.extend(num)
print("The Extended value of given list is:", fruits)  # TypeError: 'int' object is not iterable

num_emp = [1, 2, 3, 4, 5]
emp_id = [{'0035': "kumar", '0036': "shiva", '0037': "karthick", '0038': "karthi"}] # case 1: dict inside a list
num_emp.extend(emp_id)
print("The value of list after using extend method:", num_emp)  # it gives dict format inside method.

num_emp = [1, 2, 3, 4, 5]
emp_id = {'0035': "kumar", '0036': "shiva", '0037': "karthick", '0038': "karthi"}  # case 2:Extending dict into the list
num_emp.extend(emp_id)
print("The value of list after using extend method:", num_emp)  # it gives only key
