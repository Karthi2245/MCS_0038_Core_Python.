"""
A date in Python is not a data type of its own, but we can import a module
named datetime to work with dates as date objects.
"""
# program to display current date and time
import datetime

x = datetime.datetime.now()
print(x)

# program to get current date
import datetime

date_object = datetime.date.today()
print(date_object)

"""
In this program, we have used today() method defined in the date class to get 
a date object containing the current local date."""

"""What's inside datetime?

We can use dir() function to get a list containing all attributes of a module.
"""

import datetime

print(dir(datetime))

"""
Commonly used classes in the datetime module are:

date Class
time Class
datetime Class
timedelta Class """

# Date Object to represent a date

import datetime
d = datetime.date(2019, 4, 13)
print(d)


from datetime import date
a = date(2019, 4, 13)
print(a)

# Output for the above two program is  2019-04-13

# program to get Current Date

from datetime import date

today = date.today()

print("Current date =", today)

"""Print today's year, month and day
We can get year, month, day, day of the week etc. from the date object easily.
"""


from datetime import date

# date object of today's date
today = date.today()

print("Current year:", today.year)
print("Current month:", today.month)
print("Current day:", today.day)

# Time object to represent time

from datetime import time

# time(hour = 0, minute = 0, second = 0)
a = time()
print("a =", a)

# time(hour, minute and second)
b = time(11, 34, 56)
print("b =", b)

# time(hour, minute and second)
c = time(hour = 11, minute = 34, second = 56)
print("c =", c)

# time(hour, minute, second, microsecond)
d = time(11, 34, 56, 234566)
print("d =", d)

# Print hour, minute, second and microsecond

from datetime import time

a = time(11, 34, 56)

print("hour =", a.hour)
print("minute =", a.minute)
print("second =", a.second)
print("microsecond =", a.microsecond)

# Print year, month, hour, minute and timestamp

from datetime import datetime

a = datetime(2017, 11, 28, 23, 55, 59, 342380)
print("year =", a.year)
print("month =", a.month)
print("hour =", a.hour)
print("minute =", a.minute)
print("timestamp =", a.timestamp())


"""Python strftime() - datetime object to string
The strftime() method is defined under classes date, datetime and time.
The method creates a formatted string from a given date, datetime or time 
object."""

# Format date using strftime()

from datetime import datetime

# current date and time
now = datetime.now()

t = now.strftime("%H:%M:%S")
print("time:", t)

s1 = now.strftime("%m/%d/%Y, %H:%M:%S")
# mm/dd/YY H:M:S format
print("s1:", s1)

s2 = now.strftime("%d/%m/%Y, %H:%M:%S")
# dd/mm/YY H:M:S format
print("s2:", s2)

"""Here, %Y, %m, %d, %H etc. are format codes. The strftime() method takes one 
or more format codes and returns a formatted string based on it.

In the above program, t, s1 and s2 are strings.

%Y - year [0001,..., 2018, 2019,..., 9999]
%m - month [01, 02, ..., 11, 12]
%d - day [01, 02, ..., 30, 31]
%H - hour [00, 01, ..., 22, 23
%M - minute [00, 01, ..., 58, 59]
%S - second [00, 01, ..., 58, 59   """

