'''
Date : 19th April 2024
Desc : Split string into equal window
'''

sentence= str(input('Enter a string : '))

mid= len(sentence)//2

print('First half is  : ',sentence[:mid])
print('Second half is : ',sentence[mid:])
