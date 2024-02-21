import timeit
import random

# Функція сортування злиттям 
def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left_half = merge_sort(arr[:mid])
    right_half = merge_sort(arr[mid:])
    return merge(left_half, right_half)

# Функція злиття двох відсортованих списків
def merge(left, right):
    result = []
    left_index, right_index = 0, 0
    while left_index < len(left) and right_index < len(right):
        if left[left_index] < right[right_index]:
            result.append(left[left_index])
            left_index += 1
        else:
            result.append(right[right_index])
            right_index += 1
    result.extend(left[left_index:])
    result.extend(right[right_index:])
    return result

# Функція сортування вставками
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

# Генерація тестових даних
test_data = [random.randint(0, 1000) for _ in range(1000)]

# Вимірювання часу сортування методом злиття
merge_sort_time = timeit.timeit(lambda: merge_sort(test_data.copy()), number = 1)

# Вимірювання часу сортування методом вставки
insertion_sort_time = timeit.timeit(lambda: insertion_sort(test_data.copy()), number = 1)

# Вимірювання часу сортування Timsort
timsort_time = timeit.timeit(lambda: sorted(test_data.copy()), number = 1)

print(f"Час сортування методом злиття: {merge_sort_time} секунд")
print(f"Час сортування методом вставки: {insertion_sort_time} секунд")
print(f"Час сортування Timsort: {timsort_time} секунд")