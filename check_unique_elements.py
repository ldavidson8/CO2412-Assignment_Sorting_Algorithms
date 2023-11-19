def check_unique_elements(array):
    unique_set = set()

    for num in array:
        if num in unique_set:
            return False  # Found a duplicate
        unique_set.add(num)
    return True