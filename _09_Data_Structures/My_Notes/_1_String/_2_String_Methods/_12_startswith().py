'''
startswith():
--> The startswith() method returns True if a string starts with the specified
prefix(string). If not, it returns False.
'''
# Ex:
message = 'Python is fun'
print(message.startswith('Python'))

# startswith() Without start and end Parameters:
text = "Python is easy to learn."

result = text.startswith('is easy')

print(result)

result = text.startswith('Python is ')

print(result)

result = text.startswith('easy to learn.')

print(result)

# startswith() With start and end Parameters
text = "Python programming is easy."

result = text.startswith('programming is', 7)

print("The result for the given string", ':', result)

result = text.startswith('programming is', 7, 18)

print(result)

result = text.startswith('program is easing easy', 7, 18)

print(result)

# startswith() With Tuple Prefix:
text = "programming is easy"

result = text.startswith(('python', 'programming'))

print(result)

result = text.startswith(('is', 'easy', 'java'))

print(result)

result = text.startswith(('programming', 'easy'), 12, 19)

print(result)