'''
replace():

Replaces all occurrences of old in string with new or at most max occurrences
if max given.

'''
# Ex: 1
text = 'bat ball'
# replace b with c
replaced_text = text.replace('b', 'c')
print("The new text".ljust(40, '.'), ':', replaced_text)

# Ex: 2
song = 'cold, cold heart'
# replacing 'cold' with 'hurt'
print(" The new one".ljust(40, '.'), ':', song.replace('cold', 'hurt'))

song = 'Let it be, let it be, let it be, let it be'

# replacing only two occurences of 'let' using count value
print(" The new one".ljust(40, '.'), ':', song.replace('let', "don't let", ))

# Ex: 3
song = 'cold, cold heart'
replaced_song = song.replace('o', 'e')

# The original string is unchanged
print('Original string:'.ljust(40, '.'), ':', song)

print('Replaced string:'.ljust(40, '.'), ':', replaced_song)

song = 'let it be, let it be, let it be'

# maximum of 0 substring is replaced
# returns copy of the original string
print(" The original string".ljust(40, '.'), ':',song.replace('let', 'so', 0))

