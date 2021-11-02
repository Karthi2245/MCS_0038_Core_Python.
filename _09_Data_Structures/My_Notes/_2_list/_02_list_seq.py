'''
Sequence Operation of List:
--> indexing
--> slicing
--> adding
--> multiplying
--> checking for membership

In addition, Python has built-in functions for,

6.	len() : finding the length of a sequence
7.	max() : for finding its largest element
8.	min() : for finding its smallest elements.

'''
# Indexing
numbers = [1, 2, 3, 4, 5, 6, 7]
print("The Given list is:", numbers)
print("Value of the given Index is:", numbers[3])

strings = ["Karthi", "Karthick", "Sathis", "kumar", "Shiva"]
print("The value of the given string is:", strings)
print("Value of the given index is:", strings[2])
print("The value of the particular string is:", strings[3][2])

mul_list = ["Karthi", [2, 3, 4, 5], 10, 12, ('a', 'b', 'c', 'd')]
print("The Given string is:", mul_list)
print("The negative of the given list is:", mul_list[4][-2])
print("The negative of the given list is:", mul_list[-4][2])
print("The negative of the given list is:", mul_list[-3])

# Slicing:

numbers = [1, 2, 3, 4, 5, 6, 7]
print("The Given list is:", numbers)
print("Value of the given Slicing is    :", numbers[3:])   # Print the value from given index
print("The value of the given slicing is:", numbers[:3])  # Neglect the Index value
print("The Value of the given slicing is ", numbers[1:3])  # includes first index value and not last given index value
print("The value of the given slicing is:", numbers[::])  # Empty double slicing just copy the value as slicing.
print("The value of the given slicing is:", numbers[::1])  # Double slicing with value prints accordance to its value.
print("The value of the given slicing is:", numbers[::2])  # Skips one value
print("The value of the given slicing is:", numbers[::3])  # skips two value
print("The value of the given slicing is:", numbers[2:-4])  # Skips two value
print("The value of the given slicing is:", numbers[-4:-3])  # second index value should be higher in neg slicing.
print("The value of the given slicing is:", numbers[-1:-2])  # It gives Empty list

# adding:
list1 = [1, 2, 3, 4]
list2 = [2, 4, 6, 8]
x = list1 + list2
print("before adding:", list1)
print("before adding:", list2)
print("after adding:", x)

list1 = ['a', 'b', 'c', 'd']
list2 = [1, 2, 3, 4]
x = list1 + list2
print("After adding the two list:", x)  #  list is a sequence of different type of elements.

multi_list = ["Karthi", [2, 3, 4, 5], 10, 12, ('a', 'b', 'c', 'd')]
my_list = [(1, 2), (3, 4)]
combined_list = multi_list + my_list
print("Adding of list of two tuple:", combined_list)

# Multiplying:

num_list = [1, 2, 3, 4, 5]
new_list = num_list * 5
print("The Given List is:", num_list)
print("The list after multiplying:", new_list)

# Membership :

emp_id = ["MCS-0035", "MCS-0036", "MCS-0037", "MCS-0038"]
print("The Value given list is;", emp_id)
print("Checking list With Membership operator:", "MCS-0038" in emp_id)  # can only check with the direct value
print("Checking list With Membership operator:", "MCS-0038" not in emp_id)  # not with Index

# Built in method:
mul_list = ["Karthi", [2, 3, 4, 5], 10, 12, ('a', 'b', 'c', 'd')]
print("The Length of the given List is:", len(mul_list))
print("The maximum value of the given string is:", max(mul_list))  #TypeError: '>' not supported between instances of 'list' and 'str'

num_list = [10, 25, 12, 8, 5]
print("The Maximum value of the Given list is:", max(num_list))
print("The Minimum value of the given list is:", min(num_list))



