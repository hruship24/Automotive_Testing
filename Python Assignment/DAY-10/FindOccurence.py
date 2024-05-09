'''
Desc : Task 1: Use Python's re module to find all occurrences
of the word "Python" in a given text.
'''

import re

text = "Python is a powerful programming language. Python is widely used for various purposes."
pattern = r'\bPython\b'
occurrences = re.findall(pattern, text)

print("Occurrences of 'Python':", occurrences)