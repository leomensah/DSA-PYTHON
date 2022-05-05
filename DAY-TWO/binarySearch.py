def binarySearch(array, left, right, target):
    if left > right:
        return -1
    mid = left + (right - left) // 2
    if array[mid] == target:
        return mid
    if array[left] < target:
        return binarySearch(array, left, mid-1, target)
    else:
        return binarySearch(array, mid+1, right, target)

array = [-1, 0, 1, 2, 3, 4, 7, 9, 10, 20]
target = 10
print(binarySearch(array, 0, len(array)-1, target))