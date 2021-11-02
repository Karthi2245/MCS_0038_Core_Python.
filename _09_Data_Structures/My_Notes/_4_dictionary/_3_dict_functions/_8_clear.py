'''
clear():
-->The clear() method removes all items from the dictionary.

-->The syntax of clear() is: dict.clear

-->clear() method doesn't take any parameters.
-->clear() method doesn't return any value (returns None).


'''
d = {1: "one", 2: "two"}
d.clear()
print('d =', d)


dict1 = {1: 'a', 2: 'b', 3: 'c', 4: 'd'}
dict1[5] = 'e'
print("Updated dict".ljust(40, '.'), ':', dict1, id(dict1))
del dict1[3]
print("Updated dict".ljust(40, '.'), ':', dict1)
dict1.clear()                               # clear() gives empty dictionary.
print("Updated dict".ljust(40, '.'), ':', dict1, type(dict1), id(dict1))
del dict1                                   # del keyword deletes whole dictionary.
dict1.clear()                               # NameError: name 'dict1' is not defined
print("Updated dict".ljust(40, '.'), ':', dict1, type(dict1))



