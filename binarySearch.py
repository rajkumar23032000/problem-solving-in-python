'''
This a program to search an element in a array using binary search.
If the array contains duplicate elements, it will return the first instance of the element found
'''

def binarySearch(arr, low, high, ele):
    if(high >= low):
        mid = (low + high) // 2
        if(arr[mid] == ele):
            return mid
        elif(arr[mid] > ele):
            return binarySearch(arr, low, high-1, ele)
        elif(arr[mid] < ele):
            return binarySearch(arr, low+1, high, ele)
    else:
        return -1

arr1 = list(map(int, input("Enter the elements: ").strip().split()))
element = int(input("Enter the element to be searched: "))
arr1.sort()
print("The given array after sorting: ", arr1)
result = binarySearch(arr1,0,len(arr1)-1,element)

if(result != -1):
    print("Element is present at index %d" %result)
else:
    print("Element not present")
