'''
--> In Python, a function is a group of related statements that performs a
    specific task.

--> Functions help break our program into smaller and modular chunks. As our
program grows larger and larger, functions make it more organized and manageable

--> Furthermore, it avoids repetition and makes the code reusable.

    STATE                                       BEHAVIOR
    (Data structures)                            (Functions)

--> Function is a block of  code which is used to organize the functional code
--> We can call a particular section of program by calling the function which
means write the function once and call it wherever u want.
-->It is mainly used for code re-usability.
Types:
--> Function has two types.
    --> built in  Function (Ex:print(),id(),type(),int(),float(),str(),boolean()
'''
# Define a Function:
def sum(p1, p2):   # function name should be verb or adverb not noun.
    " Doc string - which has the function meaning of the function"
    x = p1 + p2
    print("Addition of the given function".ljust(40, '.'),':', x)
sum(23,25)

def greet(name):
    """
    This function greets to
    the person passed in as
    a parameter
    """
    print("Hello, " + name + ". Good morning!")
greet('Paul')

#  In python, the function definition should always be present before the
#  function call.

# function call
greet('Paul')

# function definition
def greet(name):
    """
    This function greets to
    the person passed in as
    a parameter
    """
    print("Hello, " + name + ". Good morning!")

# Error: name 'greet' is not defined
