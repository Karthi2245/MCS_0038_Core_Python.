'''
update():
The update() method updates the dictionary with the elements from
another dictionary object or from an iterable of key/value pairs.
-->

'''

marks = {'Physics': 67, 'Maths': 87}
internal_marks = {'Practical': 48}
marks.update(internal_marks)
print("The updated dict is".ljust(40, '.'), ':', marks)

d = {1: "one", 2: "three"}
d1 = {2: "two"}                   # updates the existing value of key 2
d.update(d1)
print("The value of d".ljust(40, '.'), ':', d)
d1 = {3: "three"}                 # adds element with key 3
d.update(d1)
print("The value of d".ljust(40, '.'), ':', d)

# update() When Tuple is Passed:

d = {'x': 2}
d.update(y=3, z=0)   # Key is immutable:
print("The value of d".ljust(40, '.'), ':', d)
