def two_sum_sorted(arr: list, target: int) -> None | tuple[int, int]:
    left = 0
    right = len(arr) - 1

    while left <= right:
        s = arr[left] + arr[right]

        if s == target:
            return left, right
        elif s < target:
            left += 1
        elif s > target:
            right -= 1

    return None
