'''
Date   : 18th April 2024
Author : Hrushi Pawar
Desc   : Simple Calculator
'''

while True:
    num1 = int(input('\nEnter the first number : '))
    num2 = int(input('Enter the second number : '))

    print('\nEnter your choice of operation\'s number you want to perform (1 to 4): ')
    print('1. Addtion \n2. Subtraction \n3. Multiplication \n4. Division\n5. Exit')

    choice = int(input(':-> '))

    match choice:
        case 1:
            print('\nAddition of ',num1 ,' and ', num2,' is ', num1+num2)
        case 2:
            print('\nSubtraction of ',num1 ,' and ', num2,' is ', num1-num2)
        case 3:
            print('\nMultiplication of ',num1 ,' and ', num2,' is ', num1*num2)
        case 4:
            if num2 == 0:
                print('\nDivide can not be possible')
            else:
                print('\nDivision of ',num1 ,' and ', num2,' is ', num1+num2)
        case 5:
            print('\nProgram Exited Successfully')
            break
        case _:
            print('Invalid Input')
    print('\nDo you wish to Continue ')
    print('Press 1 to continue and any number to exit')
    wish=int(input(':-> '))
    if(wish !=1):
        print('\nProgram Exited Successfully')
        break
        







            

