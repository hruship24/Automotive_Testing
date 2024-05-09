
numerator = int(input('Enter a numenator : '))
denominator = int(input('Enter denomenator : '))
list1=[1,2,3,4,5]

try :
    res = numerator // denominator
    print('Division is ',res)
    print(list1[8])

except ZeroDivisionError :
    print('Can not be devided by Zero !!!')
except Exception as e :
    print(e)

print('Code Executed ...!!!')