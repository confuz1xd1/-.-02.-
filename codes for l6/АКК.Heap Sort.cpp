#include <iostream>
using namespace std;

// Функция для поддержания свойства max-кучи
void heapify(int arr[], int n, int i) {
    int largest = i;       // Наибольший элемент — корень
    int left = 2 * i + 1;  // Левый потомок
    int right = 2 * i + 2; // Правый потомок

    // Если левый потомок больше корня
    if (left < n && arr[left] > arr[largest])
        largest = left;

    // Если правый потомок больше текущего наибольшего
    if (right < n && arr[right] > arr[largest])
        largest = right;

    // Если наибольший элемент не корень
    if (largest != i) {
        swap(arr[i], arr[largest]);
        // Рекурсивно heapify для поддерева
        heapify(arr, n, largest);
    }
}

// Основная функция для выполнения пирамидальной сортировки
void heapSort(int arr[], int n) {
    // Построение кучи (перегруппировываем массив)
    for (int i = n / 2 - 1; i >= 0; i--)
        heapify(arr, n, i);

    // Извлечение элементов из кучи по одному
    for (int i = n - 1; i > 0; i--) {
        // Перемещаем текущий корень в конец
        swap(arr[0], arr[i]);

        // Вызываем heapify для уменьшенной кучи
        heapify(arr, i, 0);
    }
}

// Функция вывода массива
void printArray(int arr[], int n) {
    for (int i = 0; i < n; i++)
        cout << arr[i] << " ";
    cout << endl;
}

// Точка входа
int main() {
    int arr[] = {12, 11, 13, 5, 6, 7};
    int n = sizeof(arr) / sizeof(arr[0]);

    cout << "Исходный массив: ";
    printArray(arr, n);

    heapSort(arr, n);

    cout << "Отсортированный массив: ";
    printArray(arr, n);

    return 0;
}
