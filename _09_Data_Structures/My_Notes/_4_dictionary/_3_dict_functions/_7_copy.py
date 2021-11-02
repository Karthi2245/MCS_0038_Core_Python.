'''
copy():
They copy() method returns a copy (shallow copy) of the dictionary.


'''
# Ex:
original_marks = {'Physics':67, 'Maths':87}
copied_marks = original_marks.copy()
print('Original Marks:', original_marks)
print('Copied Marks:', copied_marks)

# How copy works for dictionaries
original = {1:'one', 2:'two'}
new = original.copy()
print('Orignal: ', original)
print('New: ', new)
original = {1:'one', 2:'two'}
new = original


# removing all elements from the list
new.clear()

print('new: ', new)
print('original: ', original)