'''
Generator:
If a function contains at least one yield statement
(it may contain other yield or return statements), it becomes a generator
function. Both yield and return will return some value from a function.
'''
# A simple generator function
def my_gen():
    n = 1
    print('This is printed first')
    # Generator function contains yield statements
    yield n

    n += 1
    print('This is printed second')
    yield n

    n += 1
    print('This is printed at last')
    yield n
# We can iterate through the items using next().
a = my_gen()
next(a)
next(a)
next(a)
# next(a)
# StopIteration
# next(a)
# StopIteration

# Using for Loop to get the value directly:
# A simple generator function
def my_gen():
    n = 1
    print('This is printed first')
    # Generator function contains yield statements
    yield n

    n += 1
    print('This is printed second')
    yield n

    n += 1
    print('This is printed at last')
    yield n


# Using for loop
for item in my_gen():
    print(item)

# Python Generators with a Loop


def rev_str(my_str):
    length = len(my_str)
    for i in range(length - 1, -1, -1):
        yield my_str[i]
# For loop to reverse the string


for char in rev_str("hello"):
    print(char)

# Python Generator Expression:
my_list = [1, 3, 6, 10]
# Initialize the list

# square each term using list comprehension
list_ = [x**2 for x in my_list]

generator = (x**2 for x in my_list)

print(list_)
print(generator)

# Initialize the list
my_list = [1, 3, 6, 10]

a = (x**2 for x in my_list)
print(next(a))
print(next(a))
print(next(a))
print(next(a))
sum(x**2 for x in my_list)
max(x**2 for x in my_list)

# Use of Generators:
# Easy to Learn
# Ex: Sequence of power of 2 using an iterator class


class PowTwo:  # using iterator:
    def __init__(self, max=0):
        self.n = 0
        self.max = max

    def __iter__(self):
        return self

    def __next__(self):
        if self.n > self.max:
            raise StopIteration

        result = 2 ** self.n
        self.n += 1
        return result


def powtwoGen(max=0):
    n = 0
    while n < max:
        yield 2 ** n
        n += 1


obj = powtwoGen()
print(obj)

# Pip line Generators:


def fibonacci_numbers(nums):
    x, y = 0, 1
    for _ in range(nums):
        x, y = y, x+y
        yield x


def square(nums):
    for num in nums:
        yield num**2


print(sum(square(fibonacci_numbers(10))))

'''
class Employee:
    emp_detail = {'A': [{'id': 'MCS-0037', 'name': 'Karthi',
                         'salary': {'basic': 9000, 'hr': 3500, 'sa': 2000}},
                        {'id': 'MCS-0038', 'name': 'Shiva',
                         'salary': {'basic': 6000, 'hr': 2200, 'sa': 1250}},
                        {'id': 'MCS-0039', 'name': 'Kumar',
                         'salary': {'basic': 5700, 'hr': 2000, 'sa': 1850}},
                        {'id': 'MCS-0040', 'name': 'Karthick',
                         'salary': {'basic': 7500, 'hr': 2500, 'sa': 1200}},
                        {'id': 'MCS-0041', 'name': 'Sathish',
                         'salary': {'basic': 8650, 'hr': 2200, 'sa': 1400}},
                        {'id': 'MCS-0042', 'name': 'Venkat',
                         'salary': {'basic': 6750, 'hr': 2150, 'sa': 1400}}
                        ], 'B':[{'fname':'Karthi', 'lname':'Ramesh', 'location':'Chennai'},
                    {'fname': 'Shiva', 'lname': 'Prasad', 'location': 'Hydrabad'},
                    {'fname': 'Kumar', 'lname': 'Aanand', 'location': 'Royal seema'},
                    {'fname': 'Karthick', 'lname': 'Raja', 'location': 'Madurai'},
                    {'fname': 'Sathish', 'lname': 'Katta', 'location': 'VisahaPattinam'},
                                {'fname': 'Venkat', 'lname': 'Reddy',
                                 'location': 'Banglore'}
                    ]
               }
    # Even Number of Employees:

    def emp_even(self):

        a = Employee.emp_detail['A']

        for i in range(len(a)):
            for k, y in a[i].items():
                if i % 2 != 0:
                    if k == 'id' or k == 'name':
                        print('even employees', k, ':', y)

    def all_emp(self):
        a = Employee.emp_detail['A']
        print('all Employees', a)
    def emp_sal(self):

        for i in Employee.emp_detail['A']:
            list1 = []
            b =i['salary']
            for j in b:
                list1.append(b[j])
            print(i['name'], sum(list1))


obj = Employee()
obj.emp_even()
obj.all_emp()
obj.emp_sal()


class Employee2(Employee):

    def fname(self):
        for i in Employee2.emp_detail['B']:
            a = i['fname']
            print(a)
    def lname(self):
        for i in Employee2.emp_detail['B']:
            a = i['lname']
            print(a)

    def location(self):
        list1 = []
        list2 = []
        for i in Employee2.emp_detail['A']:
            list1.append(i['id'])
        for j in Employee2.emp_detail['B']:
            list2.append(j['location'])
        for a , b in zip(list1, list2):
            print(a,':', b)


#for i in Employee2.emp_detail['B']:
#a = i['location']
#print( Employee2.emp_detail['A'][0]['id'], a)

    def emp_sal(self):

        for i in Employee2.emp_detail['A']:
            list1 = []
            b =i['salary']
            for j in b:
                list1.append(b[j])
                total = sum(list1)
                if total > 10000:
                    print(i['name'], total)
                    break



obj2 = Employee2()
print('........First Name........')
obj2.fname()
print('........Last Name.........')
obj2.lname()
print('........Location.........')
obj2.location()
print('........Salary.........')
obj2.emp_sal()'''
