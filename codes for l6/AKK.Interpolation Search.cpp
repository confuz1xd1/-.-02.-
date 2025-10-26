Interpolation Search

#include <iostream>
#include <vector>

// Функция интерполирующего поиска
int interpolationSearch(const std::vector<int>& arr, int target) {
    int low = 0;
    int high = arr.size() - 1;

    while (low <= high && target >= arr[low] && target <= arr[high]) {
        // Формула интерполяции для нахождения позиции
        int pos = low + ((double)(high - low) / (arr[high] - arr[low])) * (target - arr[low]);

        if (arr[pos] == target)
            return pos;  // Элемент найден

        if (arr[pos] < target)
            low = pos + 1;  // Поиск справа
        else
            high = pos - 1; // Поиск слева
    }
    return -1; // Элемент не найден
}

int main() {
    std::vector<int> data = {10, 20, 30, 40, 50, 60, 70, 80, 90, 100};
    int target = 70;

    int index = interpolationSearch(data, target);

    if (index != -1)
        std::cout << "Элемент " << target << " найден по индексу: " << index << std::endl;
    else
        std::cout << "Элемент не найден." << std::endl;

    return 0;
}
