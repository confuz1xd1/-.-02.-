code3 C++

#include <iostream>
#include <vector>
using namespace std;

class BinaryHeap {
private:
    vector<int> heap;

    int parent(int i) { return (i - 1) / 2; }
    int left_child(int i) { return 2 * i + 1; }
    int right_child(int i) { return 2 * i + 2; }

    void sift_up(int i) {
        while (i > 0 && heap[parent(i)] < heap[i]) {
            swap(heap[parent(i)], heap[i]);
            i = parent(i);
        }
    }

    void sift_down(int i) {
        int size = heap.size();
        int max_index = i;
        int left = left_child(i);
        int right = right_child(i);

        if (left < size && heap[left] > heap[max_index])
            max_index = left;
        if (right < size && heap[right] > heap[max_index])
            max_index = right;
        if (max_index != i) {
            swap(heap[i], heap[max_index]);
            sift_down(max_index);
        }
    }

public:
    void insert(int key) {
        heap.push_back(key);
        sift_up(heap.size() - 1);
    }

    int extract_max() {
        if (heap.empty()) return -1;   // Можно заменить на другое поведение
        int result = heap[0];
        heap[0] = heap.back();
        heap.pop_back();
        sift_down(0);
        return result;
    }

    int get_max() const {
        if (heap.empty()) return -1;   // Можно заменить на другое поведение
        return heap[0];
    }

    int size() const {
        return heap.size();
    }
};

int main() {
    BinaryHeap bh;
    bh.insert(10);
    bh.insert(20);
    bh.insert(5);

    cout << "Максимальный элемент: " << bh.get_max() << endl;       // 20
    cout << "Извлечь максимум: " << bh.extract_max() << endl;       // 20
    cout << "Максимальный элемент после извлечения: " << bh.get_max() << endl;   // 10

    return 0;
}
==========================================================================================

Биномиальная куча
#include <iostream>
#include <climits>

struct BinomialNode {
    int key;
    int degree;
    BinomialNode* parent;
    BinomialNode* child;
    BinomialNode* sibling;

    BinomialNode(int k) : key(k), degree(0), parent(nullptr), child(nullptr), sibling(nullptr) {}
};

class BinomialHeap {
public:
    BinomialNode* head;

    BinomialHeap() : head(nullptr) {}

    // Слияние двух списков корней по степени
    BinomialNode* mergeRoots(BinomialNode* h1, BinomialNode* h2) {
        if (!h1) return h2;
        if (!h2) return h1;
        if (h1->degree <= h2->degree) {
            h1->sibling = mergeRoots(h1->sibling, h2);
            return h1;
        } else {
            h2->sibling = mergeRoots(h1, h2->sibling);
            return h2;
        }
    }

    void link(BinomialNode* y, BinomialNode* z) {
        y->parent = z;
        y->sibling = z->child;
        z->child = y;
        z->degree += 1;
    }

    BinomialNode* unionHeaps(BinomialNode* h1, BinomialNode* h2) {
        BinomialNode* newHead = mergeRoots(h1, h2);
        if (!newHead) return nullptr;

        BinomialNode* prev = nullptr;
        BinomialNode* curr = newHead;
        BinomialNode* next = curr->sibling;

        while (next) {
            if (curr->degree != next->degree ||
                (next->sibling && next->sibling->degree == curr->degree)) {
                prev = curr;
                curr = next;
            } else {
                if (curr->key <= next->key) {
                    curr->sibling = next->sibling;
                    link(next, curr);
                } else {
                    if (prev) prev->sibling = next;
                    else newHead = next;
                    link(curr, next);
                    curr = next;
                }
            }
            next = curr->sibling;
        }
        return newHead;
    }

    void insert(int key) {
        BinomialNode* node = new BinomialNode(key);
        BinomialHeap tempHeap;
        tempHeap.head = node;
        head = unionHeaps(head, tempHeap.head);
    }

    int findMin() {
        if (!head) return INT_MAX;
        BinomialNode* curr = head;
        int minKey = INT_MAX;
        while (curr) {
            if (curr->key < minKey)
                minKey = curr->key;
            curr = curr->sibling;
        }
        return minKey;
    }

    int extractMin() {
        if (!head) return INT_MAX;
        BinomialNode* minNode = head;
        BinomialNode* minPrev = nullptr;
        BinomialNode* prev = nullptr;
        BinomialNode* curr = head;
        int minKey = curr->key;
        while (curr) {
            if (curr->key < minKey) {
                minKey = curr->key;
                minNode = curr;
                minPrev = prev;
            }
            prev = curr;
            curr = curr->sibling;
        }
        // Удаление minNode из списка корней
        if (minPrev)
            minPrev->sibling = minNode->sibling;
        else
            head = minNode->sibling;

        // Переворачиваем список детей
        BinomialNode* child = minNode->child;
        BinomialNode* revChild = nullptr;
        while (child) {
            BinomialNode* next = child->sibling;
            child->parent = nullptr;
            child->sibling = revChild;
            revChild = child;
            child = next;
        }
        head = unionHeaps(head, revChild);
        return minKey;
    }
};

int main() {
    BinomialHeap bh;
    bh.insert(10);
    bh.insert(3);
    bh.insert(8);
    bh.insert(21);
    bh.insert(14);

    std::cout << "Минимальный элемент: " << bh.findMin() << std::endl;
    std::cout << "Удалён минимальный элемент: " << bh.extractMin() << std::endl;
    std::cout << "Новый минимальный элемент: " << bh.findMin() << std::endl;
    return 0;
}

==========================================================================================
Куча Фибоначчи

#include <iostream>
#include <vector>
#include <climits>
#include <cmath>

struct Node {
    int key;
    int degree;
    bool mark;
    Node* parent;
    Node* child;
    Node* left;
    Node* right;

    Node(int k) : key(k), degree(0), mark(false), parent(nullptr), child(nullptr),
                  left(this), right(this) {}
};

class FibonacciHeap {
public:
    FibonacciHeap() : min(nullptr), count(0) {}

    Node* insert(int key) {
        Node* node = new Node(key);
        if (!min) {
            min = node;
        } else {
            // Вставка в корневой список
            node->left = min;
            node->right = min->right;
            min->right->left = node;
            min->right = node;
            if (key < min->key)
                min = node;
        }
        ++count;
        return node;
    }

    void merge(FibonacciHeap& other) {
        if (!other.min) return;
        if (!min) {
            min = other.min;
            count = other.count;
            return;
        }
        // Объединение двух корневых списков
        min->right->left = other.min->left;
        other.min->left->right = min->right;
        min->right = other.min;
        other.min->left = min;
        if (other.min->key < min->key)
            min = other.min;
        count += other.count;
    }

    int extractMin() {
        Node* z = min;
        if (!z) return INT_MAX;
        // Переносим детей z в корневой список
        if (z->child) {
            std::vector<Node*> children;
            Node* x = z->child;
            do {
                children.push_back(x);
                x->parent = nullptr;
                x = x->right;
            } while (x != z->child);
            for (Node* c : children) {
                c->left->right = c->right;
                c->right->left = c->left;
                c->left = min;
                c->right = min->right;
                min->right->left = c;
                min->right = c;
            }
        }
        // Удаляем z из корневого списка
        z->left->right = z->right;
        z->right->left = z->left;
        if (z == z->right) {
            min = nullptr;
        } else {
            min = z->right;
            consolidate();
        }
        --count;
        int ret = z->key;
        delete z;
        return ret;
    }

    void decreaseKey(Node* x, int k) {
        if (k > x->key) throw std::invalid_argument("new key is greater than current key");
        x->key = k;
        Node* y = x->parent;
        if (y && x->key < y->key) {
            cut(x, y);
            cascadingCut(y);
        }
        if (x->key < min->key)
            min = x;
    }

    int findMin() const {
        return min ? min->key : INT_MAX;
    }

private:
    Node* min;
    int count;

    void consolidate() {
        int max_degree = 50;
        std::vector<Node*> A(max_degree, nullptr);
        std::vector<Node*> roots;
        Node* x = min;
        if (!x) return;
        do {
            roots.push_back(x);
            x = x->right;
        } while (x != min);
        for (Node* w : roots) {
            x = w;
            int d = x->degree;
            while (A[d]) {
                Node* y = A[d];
                if (x->key > y->key)
                    std::swap(x, y);
                link(y, x);
                A[d] = nullptr;
                ++d;
            }
            A[d] = x;
        }
        min = nullptr;
        for (Node* node : A) {
            if (node) {
                if (!min || node->key < min->key)
                    min = node;
            }
        }
    }

    void link(Node* y, Node* x) {
        // Удаляем y из корневого списка
        y->left->right = y->right;
        y->right->left = y->left;
        y->parent = x;
        if (!x->child) {
            x->child = y;
            y->left = y;
            y->right = y;
        } else {
            y->left = x->child;
            y->right = x->child->right;
            x->child->right->left = y;
            x->child->right = y;
        }
        ++x->degree;
        y->mark = false;
    }

    void cut(Node* x, Node* y) {
        if (x->right == x)
            y->child = nullptr;         // Эта строка отделяет x, если он единственный ребёнок
        else if (y->child == x)
            y->child = x->right;
        x->left->right = x->right;
        x->right->left = x->left;
        --y->degree;
        // Добавляем x в корневой список
        x->left = min;
        x->right = min->right;
        min->right->left = x;
        min->right = x;
        x->parent = nullptr;
        x->mark = false;
    }

    void cascadingCut(Node* y) {
        Node* z = y->parent;
        if (z) {
            if (!y->mark) {
                y->mark = true;
            } else {
                cut(y, z);
                cascadingCut(z);
            }
        }
    }
};

==========================================================================================

Хеш таблица

#include <iostream>
#include <vector>
#include <list>
#include <string>
using namespace std;

class HashTable {
private:
    int size;
    vector<list<pair<string, int>>> table; // Вектор списков пар (ключ, значение)

    int hash(const string& key) {
        // Простейшая хеш-функция: сумма кодов символов % размер таблицы
        unsigned int hashVal = 0;
        for (char c : key)
            hashVal = hashVal * 31 + c; // 31 — простое число для минимизации коллизий
        return hashVal % size;
    }

public:
    HashTable(int sz = 10) : size(sz) {
        table.resize(size);
    }

    void put(const string& key, int value) {
        int idx = hash(key);
        for (auto& kv : table[idx]) {
            if (kv.first == key) {
                kv.second = value; // обновление значения
                return;
            }
        }
        table[idx].push_back({key, value}); // добавление нового элемента
    }

    int* get(const string& key) {
        int idx = hash(key);
        for (auto& kv : table[idx]) {
            if (kv.first == key) {
                return &kv.second;
            }
        }
        return nullptr; // если ключ не найден
    }

    bool remove(const string& key) {
        int idx = hash(key);
        for (auto it = table[idx].begin(); it != table[idx].end(); ++it) {
            if (it->first == key) {
                table[idx].erase(it);
                return true;
            }
        }
        return false; // если ключ не найден
    }
};

int main() {
    HashTable ht;

    ht.put("apple", 10);
    ht.put("banana", 20);

    if (int* val = ht.get("apple"))
        cout << *val << endl;        // Выведет 10
    if (int* val = ht.get("banana"))
        cout << *val << endl;        // Выведет 20

    ht.remove("apple");
    if (int* val = ht.get("apple"))
        cout << *val << endl;
    else
        cout << "None" << endl;      // Выведет None

    return 0;
}
