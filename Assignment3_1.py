print("Accept List and print addition.......")
arr=list()
ans=0
num=input("Enter the number you want")
for i in range(0,int(num)):
    no=input("num:")
    ans=ans+int(no)
    arr.append(no)
print("The List is:::",arr)
print("The addition of all element is:",ans)