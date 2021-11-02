'''
-->The index() method returns the index of the specified element in the list.

Syntax:
list.index(element, start, end)


'''
# Ex: Returns the index value of the list element:
animals = ['cat', 'dog', 'rabbit', 'horse']
index = animals.index('dog')
print(index)


vowels = ['a', 'e', 'i', 'o', 'i', 'u']
index = vowels.index('e')
print('The index of e:', index)
index = vowels.index('i')
print('The index of i:', index)

# if index of the element not exist:
vowels = ['a', 'e', 'i', 'o', 'u']
# index = vowels.index('p')
# print('The index of p:', index)  # ValueError: 'p' is not in list

# Using index() method with end parameter:
alphabets = ['a', 'e', 'i', 'o', 'g', 'l', 'i', 'u']
index = alphabets.index('e')
print('The index of e:', index)
index = alphabets.index('i', 3)  #
print('The index of i:', index)
index = alphabets.index('i', 3, 5)   # Error! ValueError: 'i' is not in list
print('The index of i:', index)




