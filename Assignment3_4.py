print("Accept list and search that number+count....")
arr=list()
num=input("Enter number you want to print::")
print("Enter the list:")
for i in range(0,int(num)):
    n=input("num:")
    arr.append(n)
print("The List is ::",arr)
search=input("Enter the number u want to search:")
cnt=0
for i in range(len(arr)):
    if arr[i]==search:
        cnt=cnt+1
print("count::",cnt)
