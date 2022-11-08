def binary_search(self):
    low = 0
    high = len(a) - 1
    mid = 0

    while low <= high:
        mid = (high + low) // 2
        if a[mid] < x:
            low = mid + 1

        elif a[mid] > x:
            high = mid - 1

        else:
            return mid

    return -1

a = [16, 32, 41, 78, 89]
x = 32

result = binary_search(x)

if result != -1:
    print ("Element is present at index", str(result))
else:
    print("Element is not present in the array")
