
def binary_search(arr, target):
    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = (left + right) // 2  # Find the middle index

    
        if(arr[mid] == target):
            return mid 

        # If target is larger, ignore the left half
        elif(arr[mid] < target):
            left = mid + 1

        # If target is smaller, ignore the right half
        else:
            right = mid - 1

    return -1 

numbers = [10, 20, 30, 40, 50, 60, 70]

# Search for 50
result = binary_search(numbers, 50)
print(result)  # Output: 4 (index of 50)


result = binary_search(numbers, 25)
print(result)  # Output: -1