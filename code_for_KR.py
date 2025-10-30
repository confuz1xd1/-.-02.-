
Блочная (корзинная) сортировка код
=================================================================================================
def bucket_sort(arr):
    if len(arr) == 0:
        return arr

    min_value = min(arr)
    max_value = max(arr)
    bucket_count = len(arr)

    buckets = [[] for _ in range(bucket_count)]

    # Распределяем элементы по корзинам
    for num in arr:
        # Индекс корзины
        index = int((num - min_value) * (bucket_count - 1) / (max_value - min_value))
        buckets[index].append(num)

    # Сортируем внутри каждой корзины и объединяем результат
    sorted_array = []
    for bucket in buckets:
        sorted_array.extend(sorted(bucket))

    return sorted_array

# Пример использования
array = [0.42, 4.2, 3.14, 2.71, 1.41, 0.6, 2.24, 3.33]
result = bucket_sort(array)
print(result)
=================================================================================================

Блинная сортировка 
=================================================================================================
def pancake_sort(arr):
    def flip(sub_arr, k):
        start = 0
        while start < k:
            sub_arr[start], sub_arr[k] = sub_arr[k], sub_arr[start]
            start += 1
            k -= 1

    n = len(arr)
    for size in range(n, 1, -1):
        max_idx = arr.index(max(arr[:size]))
        if max_idx != 0:
            flip(arr, max_idx)
        flip(arr, size - 1)
    return arr

# Пример использования
example_arr = [3, 6, 1, 10, 5, 8]
sorted_arr = pancake_sort(example_arr)
print(sorted_arr)
=================================================================================================

Сортировка бусинами
=================================================================================================
def bead_sort(arr):
    rows = [[True]*val + [False]*(max(arr)-val) for val in arr]
    columns = list(zip(*rows))
    sorted_columns = []
    for col in columns:
        ones = sum(col)
        zeros = len(col) - ones
        sorted_col = ([True]*ones + [False]*zeros)
        sorted_columns.append(sorted_col)
    result_rows = list(zip(*sorted_columns))
    return [sum(row) for row in result_rows]

# Пример использования
arr = [5, 3, 1, 7, 4]
sorted_arr = bead_sort(arr)
print("Отсортированный массив:", sorted_arr)
=================================================================================================

Поиск скачками (Jump Search)
=================================================================================================
import math

def jump_search(arr, x):
    n = len(arr)
    
    # Вычисляем длину прыжка
    step = int(math.sqrt(n))
    
    prev = 0  # Начальная позиция
    
    while arr[min(step, n)-1] < x:
        prev = step       # Запоминаем предыдущую позицию
        step += int(math.sqrt(n))   # Двигаемся дальше
        
        if prev >= n:     # Проверяем выход за пределы массива
            return -1
            
    # Выполняем линейный поиск внутри блока
    for i in range(prev, min(step, n)):
        if arr[i] == x:
            return i
            
    return -1


# Пример использования
arr = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
target = 5
result = jump_search(arr, target)
if result != -1:
    print(f'Элемент {target} найден на индексе {result}')
else:
    print('Элемент не найден')
=================================================================================================

Экспоненциальный поиск (Exponential Search)
=================================================================================================
def binary_search(arr, left, right, x):
    """Реализация бинарного поиска."""
    while left <= right:
        mid = (left + right) // 2

        if arr[mid] == x:
            return mid
        elif arr[mid] < x:
            left = mid + 1
        else:
            right = mid - 1
    
    return -1


def exponential_search(arr, n, x):
    """
    Реализует алгоритм экспоненциального поиска.
    
    :param arr: отсортированный массив элементов
    :param n: длина массива
    :param x: искомый элемент
    :return: индекс элемента либо -1, если элемент не найден
    """
    # Начальная проверка первого элемента
    if arr[0] == x:
        return 0

    i = 1
    # Экспоненциально увеличиваем индекс, пока значение меньше искомого
    while i < n and arr[i] <= x:
        i *= 2

    # Определяем границы диапазона для бинарного поиска
    low = i // 2
    high = min(i, n - 1)

    # Выполняем бинарный поиск внутри полученного диапазона
    result = binary_search(arr, low, high, x)
    return result


# Пример использования
arr = sorted([10, 20, 40, 45, 55, 60])
n = len(arr)
target = 45

result = exponential_search(arr, n, target)
if result != -1:
    print(f'Элемент {target} найден на индексе {result}')
else:
    print('Элемент не найден')
=================================================================================================
