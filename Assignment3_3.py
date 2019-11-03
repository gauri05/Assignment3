print("Accept list and print minimum number....")
arr=list()
num=input("Enter number you want to print::")
print("Enter the list:")
for i in range(0,int(num)):
    n=input("num:")
    arr.append(n)
    min = arr[0]
    #print(min)
    if(min >= n):
        min=int(n)
print("The List is ::",arr)
#ret=lambda val1,val2:val1+val2
#ret=lambda int(n),max:int(n)>max
print("The minimum number is::::",min)