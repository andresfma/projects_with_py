'''
What I learned?

len()
while loops
boolean data types
comparison operators
conditions
blocks
'''
message = input('Insert your text: ')
inverse = ''

i = len(message) - 1
while i >= 0:
    inverse = inverse + message[i]
    i = i - 1

print(inverse)
