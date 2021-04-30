'''
Given an array A[] and a number x, check whether there exists a pair in A[] with sum as x
'''

def checkPair(arr, Sum):
    arr.sort()
    l = 0
    r = len(arr)-1
    while(l < r):
        if(arr[l] + arr[r] == Sum):
            return 1
        elif(arr[l] + arr[r] < Sum):
            l = l+1
        else:
            r = r - 1
    return 0
    

arr1 = list(map(int, input("Enter the elements: ").strip().split()))
s = int(input("Enter the sum: "))
if(checkPair(arr1, s)):
    print("Pair exists.")
else:
    print("Pair does not exist.")
    
