C++ лр5
#include <iostream>
using namespace std;

int findMax(int arr[], int size) {
    if (size == 1) {
        return arr[0];
    } else {
        int maxRest = findMax(arr + 1, size - 1);
        return (arr[0] > maxRest) ? arr[0] : maxRest;
    }
}

int main() {
    int numbers[] = {3, 7, 2, 8, 5};
    int size = sizeof(numbers) / sizeof(numbers[0]);
    cout << "Максимальный элемент: " << findMax(numbers, size) << endl;
    return 0;
}
