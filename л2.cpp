Вложенный список имен (через vector<vector<string>>)

#include <iostream>
#include <vector>
using namespace std;

int main() {
    vector<string> names1 = {"Артемий", "Тимур"};
    vector<string> names2 = {"Артем", "Даня"};
    vector<string> names3 = {"Захар", "Ежик"};
    vector<vector<string>> groups = {names1, names2, names3};

    for (const auto& group : groups) {
        for (const auto& name : group) {
            cout << name << " ";
        }
        cout << endl;
    }
    return 0;
}


Очередь (FIFO) через std::queue

#include <iostream>
#include <queue>
using namespace std;

int main() {
    queue<int> q;
    for (int i = 1; i < 4; ++i) {
        q.push(i);
    }
    while (!q.empty()) {
        cout << q.front() << endl;
        q.pop();
    }
    return 0;
}


Дек (двусторонняя очередь) через std::deque
cpp
#include <iostream>
#include <deque>
#include <string>
using namespace std;

int main() {
    deque<string> tasks = {"task1", "task2", "task3"};
    tasks.push_front("urgent_task");
    while (!tasks.empty()) {
        cout << tasks.back() << endl;
        tasks.pop_back();
    }
    return 0;
}

Приоритетная очередь через std::priority_queue (минимальный приоритет первым)

#include <iostream>
#include <queue>
#include <vector>
#include <string>
using namespace std;

int main() {
    priority_queue<pair<int, string>, vector<pair<int, string>>, greater<pair<int, string>>> tasks;
    tasks.push({2, "mid-priority item"});
    tasks.push({1, "high-priority item"});
    tasks.push({3, "low-priority item"});

    while (!tasks.empty()) {
        auto [priority, item] = tasks.top();
        cout << "Выполняется: " << item << " с приоритетом " << priority << endl;
        tasks.pop();
    }
    return 0;
}



минимальная бинарная куча

#include <iostream>
#include <queue>
#include <vector>
#include <string>

using namespace std;

int main() {
    priority_queue<pair<int, string>, vector<pair<int, string>>, greater<pair<int, string>>> priority_queue;

    priority_queue.push({2, "Задача средней важности"});
    priority_queue.push({1, "Срочная задача"});
    priority_queue.push({3, "Обычная задача"});
    priority_queue.push({4, "Малозначимая задача"});

    while (!priority_queue.empty()) {
        auto [priority, task] = priority_queue.top();
        cout << "Выполняется: " << task << " с приоритетом " << priority << endl;
        priority_queue.pop();
    }
    return 0;
}

