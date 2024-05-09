#stub
def fibo(num,f1,f2):
    print(f1, f2, end=' ')
    for n in range (3,num+1):
        f3= f1+f2
        print(f3,end=' ')
        f1=f2
        f2=f3

#driver
num = int (input('Enter a number : '))
f1=0
f2=1
fibo(num,f1,f2)