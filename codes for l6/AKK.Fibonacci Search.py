Fibonacci Search

# Реализация алгоритма Fibonacci Search на Python

def fib_search(arr, x):
    n = len(arr)

    # Инициализация чисел Фибоначчи
    fibMMm2 = 0  # (m-2)-е число
    fibMMm1 = 1  # (m-1)-е число
    fibM = fibMMm2 + fibMMm1  # m-е число

    # Находим наименьшее число Фибоначчи, большее или равное n
    while fibM < n:
        fibMMm2 = fibMMm1
        fibMMm1 = fibM
        fibM = fibMMm2 + fibMMm1

    offset = -1  # смещение с начала массива

    # Пока есть элементы для проверки
    while fibM > 1:
        # Проверяем индекс в пределах массива
        i = min(offset + fibMMm2, n - 1)

        # Если x больше текущего элемента, сдвигаем диапазон вправо
        if arr[i] < x:
            fibM = fibMMm1
            fibMMm1 = fibMMm2
            fibMMm2 = fibM - fibMMm1
            offset = i

        # Если x меньше текущего элемента, сдвигаем диапазон влево
        elif arr[i] > x:
            fibM = fibMMm2
            fibMMm1 = fibMMm1 - fibMMm2
            fibMMm2 = fibM - fibMMm1

        # Элемент найден
        else:
            return i

    # Проверка на последний элемент
    if fibMMm1 and offset + 1 < n and arr[offset + 1] == x:
        return offset + 1

    # Элемент не найден
    return -1


# Пример использования
arr = [10, 22, 35, 40, 45, 50, 80, 82, 85, 90, 100, 235]
x = 235

index = fib_search(arr, x)
if index != -1:
    print("Элемент найден на индексе:", index)
else:
    print("Элемент не найден")
