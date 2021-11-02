''''''
'''
Decimal to Binary:
===================
Integer  : 137
Convert to binary===>  2| 137
                       2| 68 - 1
                       2| 34 - 0
                       2| 17 - 0 
                       2|  8 - 1 
                       2|  4 - 0
                       2|  2 - 0
                        |  1 - 0           Binary format - 10001001
 
 
 
Binary to Decimal:
=================== 
Given binary  number                :  1  0  0  0  1  0  0  1 
                                       -----------------------
position(0-7) left to right :          7  6  5  4  3  2  1  0 
                                      2  2  2  2  2  2  2  2  
Whereever 1 exists,calcuate power : ----------------------------   
                                    128  0  0  0  8  0  0  1  ==> sum => 137
                                   -----------------------------   
                        

In Python, you can simply use the "bin()" function to convert from a decimal value to its corresponding binary value.

And similarly, the "int()" function to convert a binary to its decimal value. The int() function takes as second argument the base of the number to be converted, which is 2 in case of binary numbers         
Ex:
a = 79
# Base 2(binary)
bin_a = bin(a)
print(bin_a)
print(int(bin_a, 2)) #Base 2(binary)

In Python, you can use the oct() function to convert from a decimal value to its corresponding octal value.
EX:
a = 79
# Base 8(octal)
oct_a = oct(a)
print(oct_a)
print(int(oct_a, 8))
In Python, you can use the hex() function to convert from a decimal value to its corresponding hexadecimal value.
The int() function with base 16 for the hexadecimal number system.
EX:
a = 79
# Base 16(hexadecimal)
hex_a = hex(a)
print(hex_a)
print(int(hex_a, 16))

                                                       
'''