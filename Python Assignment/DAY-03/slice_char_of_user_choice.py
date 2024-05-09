'''
Date : 19th April 2024
Desc : Slice characters of user choice and display error if slicing is not possible
'''
word  = str (input('Enter the string : '))
start = int (input('Enter the number you want  to slice from : '))
end   = int (input('Enter the end point for slicing : '))

# Length of the input string
length = len(word)

# Adjust negative indices
if start < 0:
    start += length
if end < 0:
    end += length

# Check if slicing is possible
if 0 <= start < length and 0 <= end <= length and start < end <= length:
    sliced_string = word[start:end]
    print("Sliced string:", sliced_string)
else:
    print("Slicing is not possible with the given start and end points.")

