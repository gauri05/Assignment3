from MarvellousNum import *
print("Accept list and prime number addition....")
arr=list()
num=input("Enter number you want to print::")
print("Enter the list:")
for i in range(0,int(num)):
    n=input("num:")
    arr.append(n)
print("The List is ::",arr)
sum=ListPrime(arr)
print("count::",sum)
