#bubble sort algorithm to sort the array in ascending order.

def bubbleSort(arr):
    l = len(arr)
    for i in range(0,l):
        for j in range(0,l-i-1):
            if(arr[j] > arr[j+1]):
                arr[j], arr[j+1] = arr[j+1], arr[j]

    return arr

arr1 = list(map(int, input("Enter the elements: ").strip().split()))
print(bubbleSort(arr1))
            
