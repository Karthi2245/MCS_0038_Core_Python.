'''Center:

-->Which returns centered a string:
-->center(width, fill char)
Returns a space-padded string with the original string centered to a total of width columns.

Syntax:
string.center(length , character)


'''
# Ex: padding up on string:
# Should follow the syntax otherwise it shows type error:(length, character)

name = "KARTHI"
print("Before padding up the string :", name)
print("After padding up the string  :", name.center(20, '*'))

name = "KARTHI"
print("Before padding up the string :", name)
print("After padding up the string  :", name.center(20, '*'))

# padding up on string numbers: # Just like string only

num = "1234"
print("Before padding up the string numbers :", num)
print("After Padding up the string numbers  :", num.center(30, "!"))

