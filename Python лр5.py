Python лр5  
def find_max(arr, start=0):
    if start == len(arr) - 1:
        return arr[start]
    max_rest = find_max(arr, start + 1)
    return arr[start] if arr[start] > max_rest else max_rest

# Пример использования:
numbers = [3, 7, 2, 8, 5]
print(find_max(numbers))  # Выведет 8



