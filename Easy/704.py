def bs(arr, x):
    left, right = 1, len(arr)
    while left < right:
        mid = (left + right)//2
        if x == arr[mid]:
            return mid
        else:
            if x > arr[mid]:
                left = mid + 1
            else:
                right = mid - 1
