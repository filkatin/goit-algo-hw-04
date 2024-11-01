import random
import timeit
import insertion_sort
import merge_sort
import tim_sort

# Tестові масиви
small_arr = [random.randint(0, 100) for _ in range(100)]
medium_arr = [random.randint(0, 1000) for _ in range(1000)]
large_arr = [random.randint(0, 10000) for _ in range(10000)]

# Копії масивів для кожного алгоритму, щоб усі алгоритми мали однакові початкові умови
arrays = {
    "small": (small_arr[:], small_arr[:], small_arr[:]),
    "medium": (medium_arr[:], medium_arr[:], medium_arr[:]),
    "large": (large_arr[:], large_arr[:], large_arr[:])
}

# Функція для заміру часу виконання
def measure_time(func, arr):
    return timeit.timeit(lambda: func(arr), number=1)

# Тестування алгоритмів
results = {
    "Insertion Sort": {"small": None, "medium": None, "large": None},
    "Merge Sort": {"small": None, "medium": None, "large": None},
    "Timsort": {"small": None, "medium": None, "large": None}
}

for size, (arr1, arr2, arr3) in arrays.items():
    results["Insertion Sort"][size] = measure_time(insertion_sort.insertion_sort, arr1[:])
    results["Merge Sort"][size] = measure_time(merge_sort.merge_sort, arr2[:])
    results["Timsort"][size] = measure_time(tim_sort.tim_sort, arr3[:])

# Виведення результатів
for alg, times in results.items():
    print(f"{alg} виконання:")
    for size, time_taken in times.items():
        print(f"  - {size} array: {time_taken:.6f} seconds")
