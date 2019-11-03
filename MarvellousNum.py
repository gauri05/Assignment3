def ListPrime(arr):
    sum=0
    for i in range(len(arr)):
        flag = False
        for j in range(2, int(arr[i])):
            if (int(arr[i]) % j == 0):
                flag = True  # not prime
                break
        # print(flag)
        if flag == False:
            sum = sum + int(arr[i])
    return sum