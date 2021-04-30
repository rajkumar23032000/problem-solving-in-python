
#Program for array rotation in clockwise and anticlockwise direction.


def rotateAntiClockWise(arr, d):
    for i in range(d):
        ele = arr[0]
        for i in range(0, len(arr)-1):
            arr[i] = arr[i+1]
        arr[-1] = ele
    return arr

def rotateClockWise(arr, d):
    for i in range(d):
        ele = arr[-1]
        for i in range(len(arr)-1, 0, -1):
            arr[i] = arr[i-1]
        arr[0] = ele
    return arr

arr1 = list(map(int, input("Enter the array elements: ").strip().split()))
no_of_rotations = int(input("Enter the no.of rotations: "))
choice = int(input("Enter your choice: 1.rotateClockWise 2.rotateAntiClockwise: "))
if(choice == 1):
    print(rotateClockWise(arr1, no_of_rotations))
elif(choice == 2):
    print(rotateAntiClockWise(arr1, no_of_rotations))

