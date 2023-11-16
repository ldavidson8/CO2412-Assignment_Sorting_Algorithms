import random
import timeit
import copy
import matplotlib.pyplot as plt
import numpy as np
from merge_sort import merge_sort as msort
from selection_sort import selection_sort as ssort
from quick_sort import quick_sort as qsort

NUMBER_MIN = 100000
NUMBER_MAX = 999999
SORTING_ITERATIONS = 5

def check_unique_elements(array):
    unique_set = set()

    for num in array:
        if num in unique_set:
            return False  # Found a duplicate
        unique_set.add(num)
    return True


# If you wish to create another array, add another whole number inside this array
ARRAY_SIZES = [100, 1000, 10000]

sorting_functions = [ssort, msort, qsort]

arrays = []
for size in ARRAY_SIZES:
    array = random.sample(range(NUMBER_MIN, NUMBER_MAX + 1), size)
    arrays.append(array)

# for checking each array has unique integers generated, uncomment for usage
"""for array_size, array in zip(ARRAY_SIZES, arrays):
    result = check_unique_elements(array)
    if result:
        print(f"All numbers in array of size {array_size} are unique")
    else:
        print(f"Not all numbers in array of size {array_size} are unique")
"""


# Create copies of the arrays for sorting
copy_arrays = [copy.deepcopy(array) for array in arrays]

# Dictionary to store run times for each algorithm
run_times_dict = {sort_func.__name__: [] for sort_func in sorting_functions}

# Line styles for each sorting algorithm
line_styles = {'quick_sort': '-', 'merge_sort': ':', 'selection_sort': '--'}

# Run each sorting algorithm five times and record execution time
for sort_func in sorting_functions:
    print(f"Sorting with {sort_func.__name__}")
    for array, array_size in zip(copy_arrays, ARRAY_SIZES):
        run_times = []

        for _ in range(SORTING_ITERATIONS): # Change constant for total iterations, function will return a mean of all iterations
            run_time = timeit.timeit(lambda: sort_func(array), number=1)
            run_times.append(run_time)
            print(f"Array size {array_size}, Run {len(run_times)}: {run_time:.6f} seconds")

        run_times_dict[sort_func.__name__].append(run_times)

for sort_func in sorting_functions:
    label_name = sort_func.__name__
    plt.plot(ARRAY_SIZES, [np.mean(times) for times in run_times_dict[sort_func.__name__]], label=label_name, linestyle=line_styles.get(label_name, '-'), marker='o')

plt.xlabel('Data Size')
plt.ylabel('Execution Time (seconds)')
plt.title('Algorithm Performance Comparison')
plt.legend()
plt.show()