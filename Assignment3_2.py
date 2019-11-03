print("Accept list and print maximum number....")
arr=list()
max=0
num=input("Enter number you want to print::")
print("Enter the list:")
for i in range(0,int(num)):
    n=input("num:")
    arr.append(n)
    if(int(n)>max):
        max=int(n)
print("The List is ::",arr)
#ret=lambda val1,val2:val1+val2
#ret=lambda arr:int(n)>max
print("The maximum number is::::",max)
#print("Max",ret)