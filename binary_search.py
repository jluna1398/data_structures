# Binary search
# only works if the list is sorted
# can be done recursively but for simplicity we only implemented
def Binary_search(arr, target):
    arr = sorted(arr)
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        if arr[mid] > target:
            high = mid - 1
        else:
            low = mid+1
    return None


print(Binary_search([1, 2, 3, 4, 5, 6, 7, 8, 9], 8))


