'''
Join():
-->The join() method takes all items in an iterable and joins them into one string.

-->A string must be specified as the separator.

Syntax:
string.join(iterable)
'''
# Ex:
my_list = ['abc', 'def', 'ghi', 'ijk']

x = "#".join(my_list)
print("before using join method:", my_list)  # can only used in sequence
print("After using join method :", x)

my_list = ['1', '2', '3', '4']

x = "@".join(my_list)
print("before using join method:", my_list)  # can only used in sequence
print("After using join method :", x)


my_list = 'abc', 'def', 'ghi', 'ijk'  # if we are not mentioning any symbol it will take this as "tuple"
x = "*".join(my_list)
print("before using join method:", my_list)  # can only used in sequence
print("After using join method :", x)