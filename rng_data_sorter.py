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


# If you wish to create another array, add another whole number inside this array
ARRAY_SIZES = [100, 1000, 10000]

sorting_functions = [ssort, msort, qsort]

arrays = []
for size in ARRAY_SIZES:
    array = [random.randint(NUMBER_MIN, NUMBER_MAX) for _ in range(size)]
    arrays.append(array)

# Create copies of the arrays for sorting
copy_arrays = [copy.deepcopy(array) for array in arrays]

# Dictionary to store run times for each algorithm
run_times_dict = {sort_func.__name__: [] for sort_func in sorting_functions}

# Run each sorting algorithm five times and record execution time
for sort_func in sorting_functions:
    print(f"Sorting with {sort_func.__name__}")
    for array, array_size in zip(copy_arrays, ARRAY_SIZES):
        # Record the times here, for debugging uncomment the code block below

        # time_taken = timeit.timeit(lambda: sort_func(array), number=5)
        # print(f"Array size {array_size}: {time_taken:.6f} seconds")

        
        run_times = []
        for _ in range(5):  # Run each function 5 times
            run_time = timeit.timeit(lambda: sort_func(array), number=1)
            run_times.append(run_time)
            print(f"Array size {array_size}, Run {len(run_times)}: {run_time:.6f} seconds")
        run_times_dict[sort_func.__name__].append(run_times)

for sort_func in sorting_functions:
    plt.plot(ARRAY_SIZES, [np.mean(times) for times in run_times_dict[sort_func.__name__]], label=sort_func.__name__)

plt.xlabel('Data Size')
plt.ylabel('Execution Time (seconds)')
plt.title('Algorithm Performance Comparison')
plt.legend()
plt.show()