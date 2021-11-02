'''
append():
-->The append() method appends an element to the end of the list.
Syntax:
list.append(element)


'''
# Append:
fruit = ["orange", "banana", "apple"]
print("The Given list is ", fruit)
fruit.append("lemon")
print("After Appending:", fruit)

mul_list = [1, 2, "Karthi", ('a', 'b'), [1, 2, 3, 4]]
print("The given list is:", mul_list)
mul_list.append({1: 'a', 2: 'b', 3: 'c'})
print("After Appending:", mul_list)   # using append method we can append single value and sequence as well.

# To view individual values with respect to index position:
list1 = [1, 2, 4]
list1.append(1)
list1.append(2)
list1.append("Karthi")
list1.append((1, 2, 3))
list1.append({1: 'a', 2: 'b', 3: 'c'})

for ind, val in enumerate(list1):
    print(ind, "------",  val)

print("Print the new list:", list1)



