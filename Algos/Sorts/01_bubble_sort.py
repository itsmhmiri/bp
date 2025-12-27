def bubble_sort(arr: list) -> list:
    n = len(arr)

    for i in range(n):
        swapped = False

        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:
            break
        else:
            continue

    return arr


arr_test1 = [5, 1, 4, 2, 8]
expected_test1 = [1, 2, 4, 5, 8]
result_test1 = bubble_sort(arr_test1.copy())
print(
    f"Test Case 1: Input: {arr_test1}, Expected: {expected_test1}, Got: {result_test1}"
)


arr_test2 = [1, 2, 3, 4, 5]
expected_test2 = [1, 2, 3, 4, 5]
result_test2 = bubble_sort(arr_test2.copy())
print(
    f"Test Case 2: Input: {arr_test2}, Expected: {expected_test2}, Got: {result_test2}"
)
