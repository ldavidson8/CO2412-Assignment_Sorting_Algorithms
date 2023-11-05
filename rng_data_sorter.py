import random
import timeit
import copy
from merge_sort import merge_sort as msort
from selection_sort import selection_sort as ssort
from quick_sort import quick_sort as qsort

NUMBER_MIN = 100000
NUMBER_MAX = 999999

ARRAY1_SIZE = 100
ARRAY2_SIZE = 1000
ARRAY3_SIZE = 10000

array1 = [random.randint(NUMBER_MIN, NUMBER_MAX) for _ in range(ARRAY1_SIZE)]
array2 = [random.randint(NUMBER_MIN, NUMBER_MAX) for _ in range(ARRAY2_SIZE)]
array3 = [random.randint(NUMBER_MIN, NUMBER_MAX) for _ in range(ARRAY3_SIZE)]

# Create copies of the arrays for sorting
copy_array1 = copy.deepcopy(array1)
copy_array2 = copy.deepcopy(array2)
copy_array3 = copy.deepcopy(array3)

# Run each sorting algorithm five times and record execution time
for array, array_size in [(copy_array1, ARRAY1_SIZE), (copy_array2, ARRAY2_SIZE), (copy_array3, ARRAY3_SIZE)]:
    time_taken = timeit.timeit(lambda: msort(array), number=5)
    print(f"merge_sort on array size {array_size}: {time_taken:.6f} seconds")

    time_taken = timeit.timeit(lambda: ssort(array), number=5)
    print(f"selection_sort on array size {array_size}: {time_taken:.6f} seconds")

    time_taken = timeit.timeit(lambda: qsort(array), number=5)
    print(f"quick_sort on array size {array_size}: {time_taken:.6f} seconds")