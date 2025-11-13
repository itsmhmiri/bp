def insertion_sort(arr: list) -> list:
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1

        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

    return arr


arr_test1 = [5, 1, 4, 2, 8]
expected_test1 = [1, 2, 4, 5, 8]
result_test1 = insertion_sort(arr_test1.copy())
print(
    f"Test Case 1: Input: {arr_test1}, Expected: {expected_test1}, Got: {result_test1}"
)


arr_test2 = [1, 2, 3, 4, 5]
expected_test2 = [1, 2, 3, 4, 5]
result_test2 = insertion_sort(arr_test2.copy())
print(
    f"Test Case 2: Input: {arr_test2}, Expected: {expected_test2}, Got: {result_test2}"
)
