# Arguments: sum of even numbers:

def sum_even(a , b):
    sum = 0

    for even in range(a, b +1):

        if even % 2 == 0:
            sum = sum + even
    return sum

add_even = sum_even(10, 20)
print(add_even)

# line 3 a&b are parameters
# line 12 10 , 20 are arguments
'''
sum_even = (10+20,20)
sum_even = (10*2, 20-8)  Like that we can give arguments while calling
'''



