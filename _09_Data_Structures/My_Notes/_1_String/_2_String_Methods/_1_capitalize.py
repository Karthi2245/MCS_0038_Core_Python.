'''Capitalize Method:
 It is used to Capitalize the first letter of the string:
Returns a space-padded string with the original string centered to a total of width columns.

Syntax:

string.capitalize()
'''
# Case:1
name = "karthi"
print("Before capitalizing string       :", name)
print("After capitalizing string        :", name.capitalize())

# case:2
# using symbol as the first letter of the string:

name = "@karthi"
print("Before capitalizing the string   :", name)
print("After capitalizing the string     :", name.capitalize())
# case:3
name = "kArTHi kkH"  # In this case capitalize will not convert the first letter of the second as capital letter.
print("Before capitalizing the string   :", name)
print("After capitalizing the string    :", name.capitalize())



