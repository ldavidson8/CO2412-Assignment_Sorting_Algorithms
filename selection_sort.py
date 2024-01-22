def selection_sort(arr):
    comparisons = 0
    for i in range(len(arr)):
        min_idx = i  # Stores the index of the minimum value found in the loop
        for j in range(i + 1, len(arr)):
            comparisons += 1
            if arr[j] < arr[min_idx]:
                min_idx = j  # Update the minimum value index to the index value of j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]  # Swap the values
    return arr, comparisons
