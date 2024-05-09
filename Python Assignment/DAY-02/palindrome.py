'''
Date : 18th April 2024
Desc : Check whether the string is palindrome or not
'''
word= str(input('Enter a word : '))
word=word.lower()
if (word == word[::-1]):
    print(word,' is Palindrome')
else :
    print(word,' is Not Palindrome')
