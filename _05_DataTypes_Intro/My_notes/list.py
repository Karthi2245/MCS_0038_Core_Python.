'''
List:
->A data structure that stores an ordered collection of items in Python is called a list.
->List is generally represented within square brackets.([])
->List can have a number of elements and different data types.


Methods
There are various methods supported by lists in Python:

Method:	                    Description:
append()	->    Adds an element to the end of the list.
copy()	    ->    Returns a shallow copy of the list.
pop()	    ->    Eliminates and returns an element from the list.
sort()	    ->    Sorts all elements of a list in ascending order.
reverse()	->    Reverses the order of all elements in the list.
remove()	->    Eliminates an element from the list.

'''
# Creating a List:
list1 = [1,2, 3, 4,"karthi"]
print(list1)

# slicing:
l = [1, 2, 3, 4, 5, 6]
print(l[0:7])
# o.p=[1,2,3,4,5,6]

# Printing:
l1 = [1, 2, 3, 4, 5, 6]
print(l1[:])
# Output =[1, 2, 3, 4, 5, 6]

#Indexing:
l2=[1 , 2, 3, 4, 5, 6]
print(l2[1])
print(l2[4])
print(l2[-1])

#Output:
# 2
# 5
# 6

# Nested Indexing:
l=[1,2,["Hello","World"],[5,6,7]]
l2=[6,7]
l.extend(l2)
print(l[2][1])
print(l[3][2])
print(l[3][0])


l[3][1] = 10
print(l)



