'''
Errors In python:
--> Compile Time Errors
--> Runtime Errors
--> logical Errors

Compile Time Errors:
--> These are Syntax Errors due to which a program fails to Compile.This can be
avoid by the Programmers

RunTime Errors:
--> When PVM cannot execute the byte code ,it flags runtime error.For Example
insufficient memory to store something or inability of the PVM to execute some
Statement come under runtime errors.

Logical Errors:
--> Logical Errors are not detected by either python or PVM. The programmer
solely responsible for logical errors.
--> It might be caused by wrong formula as a logic for particular program.

BaseException
 +-- Exception
      +-- ArithmeticError
      |    +-- FloatingPointError
      |    +-- OverflowError
      |    +-- ZeroDivisionError
      +-- AssertionError
      +-- ImportError
      |    +-- ModuleNotFoundError
      +-- LookupError
      |    +-- IndexError
      |    +-- KeyError
      +-- NameError
      |    +-- UnboundLocalError
      +-- OSError
      +-- RuntimeError
      +-- SyntaxError
      |    +-- IndentationError
      |         +-- TabError
      +-- SystemError
      +-- TypeError
      +-- ValueError


'''
# Ex: Compile Time Errors:
x = 2
# if x == 2
if x == 2:
    print("Its Equal")  # SyntaxError: invalid syntax

# Ex : Runtime Errors


def concat(a, b):
    c = a + b
    return c


name = concat(15, "Karthi")
# print("The concatenation of the given value is", name)
# TypeError: unsupported operand type(s) for +: 'int' and 'str'-->Runtime Error

# Ex: Logical Errors:
# Wrong Logic:


def increment(sal):
     sal = sal * 20/100  # Logical Errors
     return sal


obj = increment(10000)
print("The Revised salary is :", obj)

# Correct Logic:


def increment(sal):
    sal = sal + sal * 20 / 100
    return sal


obj = increment(10000)
print("The Revised salary is :", obj)

