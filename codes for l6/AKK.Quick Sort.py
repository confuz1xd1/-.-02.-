def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[len(arr) // 2]  # Опорный элемент
        left = [x for x in arr if x < pivot]
        middle = [x for x in arr if x == pivot]
        right = [x for x in arr if x > pivot]
        return quick_sort(left) + middle + quick_sort(right)

# Пример использования
example = [9, 3, 7, 1, 8, 2, 5]
sorted_example = quick_sort(example)
print(sorted_example)
