'''
-->The insert() method inserts an element to the list at the specified index.
Syntax:

'''

# String Lsit
vowel = ['a', 'e', 'i', 'u']
vowel.insert(3, 'o')
print('List:', vowel)

# Number list
prime_numbers = [2, 3, 5, 7]
prime_numbers.insert(4, 11)
print('List:', prime_numbers)

# Inserting a tuple:
mixed_list = [{1, 2}, [5, 6, 7]]
number_tuple = (3, 4)
number_dict = {1: 'a', 2: 'b', 3: 'c'}
mixed_list.insert(1, number_tuple)  # 1st argument - index position
mixed_list.insert(3, number_dict)   # 2nd argument - value to insert in the list
print('Updated List:', mixed_list)



