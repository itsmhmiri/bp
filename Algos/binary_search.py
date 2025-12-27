def binary_search(arr: list, target: int) -> int:
    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = (right + left) // 2

        if arr[mid] == target:
            return mid
        elif arr[mid] >= target:
            right = mid - 1
        else:
            left = mid + 1

    return -1


test_list = [1, 45, 1, 4, 6, 8, 9, 1, 4, 6, 10]
print(binary_search(test_list, 6))
print(test_list.index(6))
