'''
rstrip():

-->Removes all trailing whitespace of string.
'''

title = '<Python Programming   >'
print("before removing the spaces".ljust(40, '.'), ':', title)
print("After removing the spaces".ljust(40, '.'), ':', title.rstrip())

random_string = 'this is good    '
print(random_string.rstrip())
print(random_string.rstrip('si oo'))
print(random_string.rstrip('sid oo'))
website = 'www.programiz.com/'
print(website.rstrip('m/.'))


