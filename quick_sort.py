def quick_sort(arr):
    comparisons = 0
    if len(arr) <= 1:
        return arr, comparisons

    pivot = arr[len(arr) // 2]  # Find the middle using floor division
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]

    comparisons += len(left) + len(right)

    sorted_left, left_comparisons = quick_sort(left)
    sorted_right, right_comparisons = quick_sort(right)

    comparisons += left_comparisons + right_comparisons

    return sorted_left + middle + sorted_right, comparisons
