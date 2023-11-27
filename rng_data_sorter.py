# Import modules
import os
import random
import timeit
import copy
import matplotlib.pyplot as plt
import numpy as np

# Import sorting algorithms
from check_unique_elements import check_unique_elements
from merge_sort import merge_sort as msort
from selection_sort import selection_sort as ssort
from quick_sort import quick_sort as qsort

# Define constants
NUMBER_MIN = 100_000
NUMBER_MAX = 999_999
SORTING_ITERATIONS = 5
SORTED_ARRAYS_DIR = "sorted_arrays"
ARRAY_SIZES = [100, 1_000, 10_000]


# Creating the arrays of a random integer between 100,000 and 999,999
def generate_arrays(array_sizes):
    arrays = []
    for size in array_sizes:
        array = random.sample(range(NUMBER_MIN, NUMBER_MAX + 1), size)
        arrays.append(array)
    return arrays


def check_arrays(arrays, array_sizes):
    for array_size, array in zip(array_sizes, arrays):
        result = check_unique_elements(array)
        if result:
            print(f"All numbers in array of size {array_size} are unique")
        else:
            print(f"Not all numbers in array of size {array_size} are unique")


def sort_array(array, sort_func):
    run_times = []
    for _ in range(SORTING_ITERATIONS):
        run_time = timeit.timeit(lambda: sort_func(array), number=1)
        run_times.append(run_time)
    return run_times


def save_array(array, array_size, sort_func):
    algorithm_dir = os.path.join(SORTED_ARRAYS_DIR, sort_func.__name__)
    if not os.path.exists(algorithm_dir):
        os.makedirs(algorithm_dir)
    filename = f"sorted_array_size_{array_size}.txt"
    filepath = os.path.join(algorithm_dir, filename)
    with open(filepath, "w") as file:
        file.write("\n".join(map(str, array)))


def plot_times(run_times_dict, array_sizes, line_styles):
    for sort_func in run_times_dict:
        label_name = sort_func
        plt.plot(
            array_sizes,
            [np.mean(times) for times in run_times_dict[sort_func]],
            label=label_name,
            linestyle=line_styles.get(label_name, "-"),
            marker="o",
        )
    plt.xlabel("Data Size")
    plt.ylabel("Execution Time (seconds)")
    plt.title("Algorithm Performance Comparison")
    plt.legend()
    plt.show()


# Generate random arrays
arrays = generate_arrays(ARRAY_SIZES)

# Check if each array has unique elements
# Uncomment the following line for usage
check_arrays(arrays, ARRAY_SIZES)

copy_arrays = [copy.deepcopy(array) for array in arrays]

sorting_functions = [ssort, msort, qsort]

run_times_dict = {sort_func.__name__: [] for sort_func in sorting_functions}

line_styles = {"quick_sort": "-", "merge_sort": ":", "selection_sort": "--"}

# Sort each array using each algorithm and record the execution time
for sort_func in sorting_functions:
    print(f"Sorting with {sort_func.__name__}")
    for array, array_size in zip(copy_arrays, ARRAY_SIZES):
        run_times = sort_array(array, sort_func)

        run_times_dict[sort_func.__name__].append(run_times)

        save_array(array, array_size, sort_func)

        for i, run_time in enumerate(run_times):
            print(f"Array size {array_size}, Run {i+1}: {run_time:.6f} seconds")

# Plot the execution times of different algorithms
plot_times(run_times_dict, ARRAY_SIZES, line_styles)
