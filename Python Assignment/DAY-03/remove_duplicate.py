'''
Date : 19th April 2024
Desc : Remove duplicate from string
'''

word = str(input('Enter a String : '))
unique= ''
for char in word:  
    if char in unique:
        continue
    else:
        unique += char
    
print(unique)
