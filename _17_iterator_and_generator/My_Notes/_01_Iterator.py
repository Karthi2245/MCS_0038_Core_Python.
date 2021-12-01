'''
Iterator:
--> Iterator in Python is simply an object that can be iterated upon.
An object which will return data, one element at a time.
Iterating Through an Iterator:
--> We use the next() function to manually iterate through all the items of an
iterator. When we reach the end and there is no more data to be returned,
it will raise the StopIteration Exception.
'''
my_list = [4, 7, 0, 3]
# get an iterator using iter()
my_iter = iter(my_list)
# iterate through it using next()
print(next(my_iter))
print(next(my_iter))
print(my_iter.__next__())  # Alternative way to use next() Function
print(my_iter.__next__())
# This will raise error, no items left
# next(my_iter)

# Working of for loop for Iterators:
list1 = [2, 4, 6, 8, 10]
for i in list1:
    iter1 = iter(list1)

    print(next(iter1))
    print(next(iter1))
    print(next(iter1))
    print(next(iter1))
    print(next(iter1))

# Building Custom Iterator:


class PowTwo:
    """Class to implement an iterator
    of powers of two"""

    def __init__(self, max=0):
        self.max = max

    def __iter__(self):
        self.n = 0
        return self

    def __next__(self):
        if self.n <= self.max:
            result = 2 ** self.n
            self.n += 1
            return result
 #       else:
 #           raise StopIteration


# create an object
numbers = PowTwo(3)

# create an iterable from the object
i = iter(numbers)

# Using next to get to the next iterator element
print(next(i))
print(next(i))
print(next(i))
print(next(i))
# print(next(i))

# Python Infinite Iterator:


class InfIter:
    """Infinite iterator to return all
        odd numbers"""

    def __iter__(self):
        self.num = 1
        return self

    def __next__(self):
        num = self.num
        self.num += 2
        return num


a = iter(InfIter())
print(next(a))
print(next(a))
print(next(a))
print(next(a))