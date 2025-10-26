def insertion_sort(arr):
    # Проходим по всем элементам, начиная со второго
    for i in range(1, len(arr)):
        key = arr[i]  # текущий элемент для вставки
        j = i - 1
        # Сдвигаем элементы массива, которые больше key, вправо
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        # Вставляем key на правильное место
        arr[j + 1] = key
    return arr

# Пример использования
example = [9, 3, 5, 1, 8, 2]
result = insertion_sort(example)
print(result)
