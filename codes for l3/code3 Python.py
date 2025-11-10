code3 Python

Бинарная куча
class BinaryHeap:
    def __init__(self):
        self.heap = []

    def parent(self, i):
        return (i - 1) // 2
    
    def left_child(self, i):
        return 2 * i + 1
    
    def right_child(self, i):
        return 2 * i + 2

    def insert(self, key):
        self.heap.append(key)
        self._sift_up(len(self.heap) - 1)

    def _sift_up(self, i):
        while i > 0 and self.heap[self.parent(i)] < self.heap[i]:
            self.heap[self.parent(i)], self.heap[i] = self.heap[i], self.heap[self.parent(i)]
            i = self.parent(i)

    def extract_max(self):
        if len(self.heap) == 0:
            return None
        if len(self.heap) == 1:
            return self.heap.pop()
        max_item = self.heap[0]
        self.heap[0] = self.heap.pop()
        self._sift_down(0)
        return max_item

    def _sift_down(self, i):
        max_index = i
        left = self.left_child(i)
        right = self.right_child(i)
        size = len(self.heap)

        if left < size and self.heap[left] > self.heap[max_index]:
            max_index = left
        if right < size and self.heap[right] > self.heap[max_index]:
            max_index = right
        if max_index != i:
            self.heap[i], self.heap[max_index] = self.heap[max_index], self.heap[i]
            self._sift_down(max_index)

    def get_max(self):
        if not self.heap:
            return None
        return self.heap[0]

    def size(self):
        return len(self.heap)

# Пример использования
bh = BinaryHeap()
bh.insert(10)
bh.insert(20)
bh.insert(5)

print("Максимальный элемент:", bh.get_max())        # 20
print("Извлечь максимум:", bh.extract_max())         # 20
print("Максимальный элемент после извлечения:", bh.get_max())  # 10

==========================================================================================

Биномиальная куча
class BinomialNode:
    def __init__(self, key):
        self.key = key
        self.parent = None
        self.child = None
        self.sibling = None
        self.degree = 0

class BinomialHeap:
    def __init__(self):
        self.head = None

    def merge_roots(self, h1, h2):
        # Объединение двух списков корней по возрастанию степени
        if h1 is None:
            return h2
        if h2 is None:
            return h1
        if h1.degree <= h2.degree:
            res = h1
            res.sibling = self.merge_roots(h1.sibling, h2)
        else:
            res = h2
            res.sibling = self.merge_roots(h1, h2.sibling)
        return res

    def link(self, y, z):
        # Присоединить дерево корня y как поддерево корня z
        y.parent = z
        y.sibling = z.child
        z.child = y
        z.degree += 1

    def union(self, other_heap):
        new_heap = BinomialHeap()
        new_heap.head = self.merge_roots(self.head, other_heap.head)
        if new_heap.head is None:
            return new_heap

        prev = None
        curr = new_heap.head
        next = curr.sibling

        while next is not None:
            if (curr.degree != next.degree) or (next.sibling is not None and next.sibling.degree == curr.degree):
                prev = curr
                curr = next
            else:
                if curr.key <= next.key:
                    curr.sibling = next.sibling
                    self.link(next, curr)
                else:
                    if prev is None:
                        new_heap.head = next
                    else:
                        prev.sibling = next
                    self.link(curr, next)
                    curr = next
            next = curr.sibling
        return new_heap

    def insert(self, key):
        new_node = BinomialNode(key)
        new_heap = BinomialHeap()
        new_heap.head = new_node
        self.head = self.union(new_heap).head

    def find_min(self):
        if self.head is None:
            return None
        y = None
        x = self.head
        min_key = float('inf')
        while x is not None:
            if x.key < min_key:
                min_key = x.key
                y = x
            x = x.sibling
        return y.key

    def extract_min(self):
        if self.head is None:
            return None
        min_prev = None
        min_node = self.head
        prev_x = None
        x = self.head
        min_key = x.key

        while x is not None:
            if x.key < min_key:
                min_key = x.key
                min_prev = prev_x
                min_node = x
            prev_x = x
            x = x.sibling

        # Удаление min_node из списка корней
        if min_prev is None:
            self.head = min_node.sibling
        else:
            min_prev.sibling = min_node.sibling

        # Обработка детей min_node для создания новой кучи
        child = min_node.child
        prev_child = None
        while child is not None:
            next_child = child.sibling
            child.sibling = prev_child
            child.parent = None
            prev_child = child
            child = next_child

        new_heap = BinomialHeap()
        new_heap.head = prev_child

        self.head = self.union(new_heap).head
        return min_key

# Пример использования
bh = BinomialHeap()
bh.insert(10)
bh.insert(3)
bh.insert(8)
bh.insert(21)
bh.insert(14)

print("Минимальный элемент:", bh.find_min())  # 3
print("Удалён минимальный элемент:", bh.extract_min())  # 3
print("Новый минимальный элемент:", bh.find_min())  # 8

==========================================================================================
Куча Фибоначчи

class Node:
    def __init__(self, key):
        self.key = key
        self.degree = 0
        self.parent = None
        self.child = None
        self.left = self
        self.right = self
        self.mark = False

class FibonacciHeap:
    def __init__(self):
        self.min = None
        self.count = 0

    def insert(self, key):
        node = Node(key)
        if self.min is None:
            self.min = node
        else:
            # Вставка в корневой список
            node.left = self.min
            node.right = self.min.right
            self.min.right.left = node
            self.min.right = node
            if key < self.min.key:
                self.min = node
        self.count += 1
        return node

    def merge(self, other):
        if other.min is None:
            return
        if self.min is None:
            self.min = other.min
            self.count = other.count
            return
        # Объединение двух корневых списков
        self.min.right.left = other.min.left
        other.min.left.right = self.min.right
        self.min.right = other.min
        other.min.left = self.min
        if other.min.key < self.min.key:
            self.min = other.min
        self.count += other.count

    def extract_min(self):
        z = self.min
        if z is not None:
            # Добавляем детей z в корневой список
            if z.child is not None:
                children = []
                child = z.child
                while True:
                    children.append(child)
                    child.parent = None
                    child = child.right
                    if child == z.child:
                        break
                for c in children:
                    c.left.right = c.right
                    c.right.left = c.left
                    # Вставляем в корневой список
                    c.left = self.min
                    c.right = self.min.right
                    self.min.right.left = c
                    self.min.right = c

            # Удаление z из корневого списка
            z.left.right = z.right
            z.right.left = z.left

            if z == z.right:
                self.min = None
            else:
                self.min = z.right
                self._consolidate()
            self.count -= 1
        return z.key if z else None

    def _consolidate(self):
        max_degree = 50
        A = [None] * max_degree
        roots = []
        x = self.min
        if x is not None:
            while True:
                roots.append(x)
                x = x.right
                if x == self.min:
                    break
            for w in roots:
                x = w
                d = x.degree
                while A[d] is not None:
                    y = A[d]
                    if x.key > y.key:
                        x, y = y, x
                    self._link(y, x)
                    A[d] = None
                    d += 1
                A[d] = x
            self.min = None
            for i in range(max_degree):
                if A[i] is not None:
                    if self.min is None or A[i].key < self.min.key:
                        self.min = A[i]

    def _link(self, y, x):
        # Удаляем y из корневого списка
        y.left.right = y.right
        y.right.left = y.left
        y.parent = x
        if x.child is None:
            x.child = y
            y.left = y
            y.right = y
        else:
            y.left = x.child
            y.right = x.child.right
            x.child.right.left = y
            x.child.right = y
        x.degree += 1
        y.mark = False

    def decrease_key(self, x, k):
        if k > x.key:
            raise ValueError("new key is greater than current key")
        x.key = k
        y = x.parent
        if y is not None and x.key < y.key:
            self._cut(x, y)
            self._cascading_cut(y)
        if x.key < self.min.key:
            self.min = x

    def _cut(self, x, y):
        # Удаляем x из списка детей y
        if x.right == x:
            y.child = None
        elif y.child == x:
            y.child = x.right
        x.left.right = x.right
        x.right.left = x.left
        y.degree -= 1
        # Добавляем x в корневой список
        x.left = self.min
        x.right = self.min.right
        self.min.right.left = x
        self.min.right = x
        x.parent = None
        x.mark = False

    def _cascading_cut(self, y):
        z = y.parent
        if z is not None:
            if not y.mark:
                y.mark = True
            else:
                self._cut(y, z)
                self._cascading_cut(z)

    def find_min(self):
        return self.min.key if self.min else None

==========================================================================================

Хеш таблица

class HashTable:
    def __init__(self, size=10):
        self.size = size
        self.table = [[] for _ in range(size)]  # список списков для разрешения коллизий
    
    def _hash(self, key):
        # Простая хеш-функция по остатку от деления хеш-кода по размеру
        return hash(key) % self.size
    
    def put(self, key, value):
        index = self._hash(key)
        # Проверяем, если ключ уже есть - обновляем значение
        for i, (k, v) in enumerate(self.table[index]):
            if k == key:
                self.table[index][i] = (key, value)
                return
        # Иначе добавляем новый ключ-значение
        self.table[index].append((key, value))
    
    def get(self, key):
        index = self._hash(key)
        for k, v in self.table[index]:
            if k == key:
                return v
        return None  # если ключ не найден
    
    def remove(self, key):
        index = self._hash(key)
        for i, (k, v) in enumerate(self.table[index]):
            if k == key:
                del self.table[index][i]
                return True
        return False  # если ключ не найден

ht = HashTable()

ht.put("apple", 10)
ht.put("banana", 20)
print(ht.get("apple"))   # Выведет 10
print(ht.get("banana"))  # Выведет 20

ht.remove("apple")
print(ht.get("apple"))   # Выведет None
