'''
Date : 19th April 2024
Desc : Swap first and Last character from string
'''

word = str(input('Enter a word : '))

after_swap = word[-1] + word[1:-1] +word[0]

print(after_swap)
