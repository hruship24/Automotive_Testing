'''
Date : 18th April 2024
Desc : Count number of vowels in string
'''

sentence= str(input('Enter a string : '))

vowels ={'a','e','i','o','u'}
sentence=sentence.lower()
count=0 #for count the number of vowels

for char in sentence:
    if char in vowels:
        count+=1

print('Total number of vowels in sentence are ',count)
