def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2  # вычисляем середину массива
        if arr[mid] == target:
            return mid  # элемент найден
        elif arr[mid] < target:
            left = mid + 1  # ищем в правой половине
        else:
            right = mid - 1  # ищем в левой половине
    return -1  # элемент не найден

# Пример использования
array = [1, 3, 5, 7, 9, 11, 13]
result = binary_search(array, 7)
print(result)  # Вывод: 3
