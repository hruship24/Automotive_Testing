'''
Date : 22nd April 2024
Desc : Remove all duplicate words from a given sentence
'''
sentence = str(input('Enter a Sentence : '))


unique_sentence= ' '.join(set(sentence.split()))

print(unique_sentence)
