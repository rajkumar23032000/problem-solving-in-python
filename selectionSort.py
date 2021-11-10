size = int(input("Enter no.of elements: "))
print("Enter the array elements separated by space: ")
arr = list(map(int, input().split()))

for j in range(0, len(arr)-1):
    smallest_ele = arr[j]
    smallest_ind = j
    for i in range(j+1, len(arr)):
        if(arr[i] < smallest_ele):
            smallest_ele = arr[i]
            smallest_ind = i
    arr[j], arr[smallest_ind] = arr[smallest_ind], arr[j]

print("Array is Sorted in ascending order: ")
print(*arr, sep = " ")



