'''
Date : 19th April 2024
Desc : Convert CamelCase to SnakeCase
Ex.
Camelcase : IAmHrushikesh
Snakecase : i_am_hrushikesh
'''
camel_case = str(input('Enter camel case string : '))
snake_case =''

for char in camel_case:
    if char.isupper():
       snake_case += ('_'+char.lower() )
    else:
        snake_case +=char
print(snake_case.lstrip('_'))
