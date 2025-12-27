def selection_sort(arr: list) -> list:
    n = len(arr)

    for i in range(n - 1):
        min_ind = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_ind]:
                min_ind = j
        arr[i], arr[min_ind] = arr[min_ind], arr[i]

    return arr


arr_test1 = [5, 1, 4, 2, 8]
expected_test1 = [1, 2, 4, 5, 8]
result_test1 = selection_sort(arr_test1.copy())
print(
    f"Test Case 1: Input: {arr_test1}, Expected: {expected_test1}, Got: {result_test1}"
)


arr_test2 = [1, 2, 3, 4, 5]
expected_test2 = [1, 2, 3, 4, 5]
result_test2 = selection_sort(arr_test2.copy())
print(
    f"Test Case 2: Input: {arr_test2}, Expected: {expected_test2}, Got: {result_test2}"
)
