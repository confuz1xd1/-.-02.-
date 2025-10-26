def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i  # возвращаем индекс найденного элемента
    return -1  # если элемент не найден

arr = [3, 7, 2, 9, 5]
target = 9

result = linear_search(arr, target)
if result != -1:
    print(f"Элемент {target} найден на позиции {result}")
else:
    print(f"Элемент {target} не найден")
