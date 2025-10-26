def shell_sort(arr):
    n = len(arr)
    gap = n // 2  # начальный шаг

    while gap > 0:
        for i in range(gap, n):
            temp = arr[i]
            j = i
            while j >= gap and arr[j - gap] > temp:
                arr[j] = arr[j - gap]
                j -= gap
            arr[j] = temp
        gap //= 2  # уменьшаем шаг

    return arr


# Пример использования
example = [45, 12, 33, 10, 8, 19, 37]
result = shell_sort(example)
print(result)
