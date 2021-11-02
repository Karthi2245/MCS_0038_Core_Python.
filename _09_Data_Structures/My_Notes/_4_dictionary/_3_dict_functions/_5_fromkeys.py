'''
fromkeys():
-->The fromkeys() method creates a new dictionary from the given sequence of elements with
-a value provided by the user.
Syntax:
dictionary.fromkeys(sequence, value)
'''
# vowels keys
keys = {'a', 'e', 'i', 'o', 'u'}
vowels = dict.fromkeys(keys)
print(vowels)  # without values

# vowels keys
keys = {'a', 'e', 'i', 'o', 'u' }
value = 'vowel'
vowels = dict.fromkeys(keys, value)
print("updated dict".ljust(40, '.'), ':', vowels) # with keys and values

# Creating a dict with mutable list:
keys = {'a', 'e', 'i', 'o', 'u'}
value = [1]
vowels = dict.fromkeys(keys, value)
print("updated dict".ljust(40, '.'), ':', vowels)
value.append(2)
print("updated dict".ljust(40, '.'), ':', vowels)

# vowels keys
keys = {'a', 'e', 'i', 'o', 'u' }
value = [1]

vowels = { key : list(value) for key in keys }
# you can also use { key : value[:] for key in keys }
print("updated dict".ljust(40, '.'), ':', vowels)

# updating the value
value.append(2)
print("updated dict".ljust(40, '.'), ':', vowels)