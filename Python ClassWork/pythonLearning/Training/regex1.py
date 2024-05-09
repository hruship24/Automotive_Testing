import re

text = "The quick brown fox jumps over the lazy dog"
pattern = r"The"
match_obj = re.match(pattern, text)
print(match_obj)
if match_obj:
    print('Match found using match() : ',match_obj.group())
else:
    print('Match not found using match().')

    # USING Search()
