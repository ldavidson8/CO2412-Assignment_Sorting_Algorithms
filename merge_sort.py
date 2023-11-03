def merge_sort(arr):

    # Base case
    if len(arr) <= 1:
        return arr
    
    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]

    merge_sort(left_half)
    merge_sort(right_half)

    i = j = k = 0 # i left half pointer, j right half pointer, k sorted array pointer

    while i < len(left_half) and j < len(right_half):
        if left_half[i] < right_half[j]:
            # If left half value is smaller than right half, place into sorted array
            arr[k] = left_half[i] 
            i += 1
        else:
            # Right half value is smaller and placed into array
            arr[k] = right_half[j]
            j += 1
        k += 1

    # Remaining elements of left and right half is placed into array
    while i < len(left_half):
        arr[k] = left_half[i]
        i += 1
        k += 1

    while j < len(right_half):
        arr[k] = right_half[j]
        j += 1
        k += 1
