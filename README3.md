		Бинарная куча
	Определение:
Бинарная (двоичная) куча — это полное бинарное дерево, где значение в каждой вершине не меньше (или не больше — в случае min-кучи) значений её потомков, а все уровни кроме последнего заполнены полностью, а последний заполняется слева направо без пропусков.​
	Анализ кода
1) Определение класса
```
class BinaryHeap:
    def __init__(self):
        self.heap = []
```
Создаём класс BinaryHeap — это будет наша структура данных.
В конструкторе __init__ создаётся пустой список self.heap, где хранятся все элементы кучи (фактически — массив для "навигации" по дереву).
2) Навигация по массиву-куче
```
    def parent(self, i):
        return (i - 1) // 2
    def left_child(self, i):
        return 2 * i + 1
    def right_child(self, i):
        return 2 * i + 2
```
В этих функциях реализована индексация:
Родитель: для любого индекса i, родителя ищем как (i - 1) // 2
Левый потомок: 2 * i + 1
Правый потомок: 2 * i + 2
Такая индексация работает, если хранить дерево в списке: первый элемент — корень, потомки — по расчету.
3) Вставка элемента
```
    def insert(self, key):
        self.heap.append(key)
        self._sift_up(len(self.heap) - 1)
```
Добавляем новый элемент (append) в конец списка.
Затем вызываем _sift_up, чтобы поднять элемент вверх до нужного места (восстановить свойство кучи).
4) Восстановление кучи вверх
```
    def _sift_up(self, i):
        while i > 0 and self.heap[self.parent(i)] < self.heap[i]:
            self.heap[self.parent(i)], self.heap[i] = self.heap[i], self.heap[self.parent(i)]
            i = self.parent(i)
```
Пока индекс не нулевой (не корень), сравниваем элемент с родителем.
Если родитель меньше, меняемся местами — так элемент поднимается вверх по дереву к корню, если его значение больше.
После обмена индекс перемещается в новое место родителя.
5) Извлечение максимума
```
    def extract_max(self):
        if len(self.heap) == 0:
            return None
        if len(self.heap) == 1:
            return self.heap.pop()
        max_item = self.heap[0]
        self.heap[0] = self.heap.pop()
        self._sift_down(0)
        return max_item
```
Если куча пуста — возвращаем None
Если один элемент — просто pop()
Если больше: берём корень (max_item = self.heap[0]) — это самый большой элемент (Max Heap).
Последний элемент переставляем на место корня (self.heap[0] = self.heap.pop()), а затем восстанавливаем структуру кучи вниз (_sift_down(0)).
6. Восстановление кучи вниз
```
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
```
Сравниваем элемент с его потомками.
Если какой-то потомок больше — меняемся с ним местами.
Процесс продолжается рекурсивно, пока элемент не окажется на правильной позиции.
7) Получение максимального элемента
```
    def get_max(self):
        if not self.heap:
            return None
        return self.heap[0]
```
Если куча не пуста — возвращаем корень, он всегда максимальный в Max Heap.
8) Получение размера кучи
python
    def size(self):
        return len(self.heap)
Просто возвращаем количество элементов в куче.

		Биномиальная куча
	Определение 
Биномиальная куча — это структура данных, реализующая абстрактный тип данных «очередь с приоритетом». Она представляет собой набор биномиальных деревьев, которые обладают двумя основными свойствами: ключ каждой вершины не меньше ключа её родителя, и все биномиальные деревья имеют разный размер. Каждый биномиальный дерево ранга k содержит 2^k вершин и определяется рекурсивно: дерево ранга 0 состоит из одной вершины, а дерево ранга k строится из двух деревьев ранга k−1, одно из которых подвешивается к корню другого. Благодаря этим свойствам, корень каждого дерева в куче содержит минимальный ключ среди всех его вершин.
	Анализ кода 
1) Класс BinomialNode
```
class BinomialNode:
    def __init__(self, key):
        self.key = key
        self.parent = None
        self.child = None
        self.sibling = None
        self.degree = 0
```
Каждый элемент кучи представлен объектом этого класса.
Атрибуты:
key — значение элемента,
parent, child, sibling — связи для построения биномиальных деревьев,
degree — степень дерева (количество потомков).
2) Класс BinomialHeap
```
class BinomialHeap:
    def __init__(self):
        self.head = None
```
Основная структура для самой кучи, где head указывает на начало списка корней биномиальных деревьев.
3) Объединение списков корней (merge_roots)
```
def merge_roots(self, h1, h2):
```
Использует рекурсию для объединения двух списков корней по возрастанию степени.
Основная логика: выбирай дерево с меньшей degree из двух и присоединяй к нему объединённый остаток списков.
4) Сцепка деревьев (link)
```
def link(self, y, z):
    y.parent = z
    y.sibling = z.child
    z.child = y
    z.degree += 1
```
Делает одно дерево поддеревом другого, обновляет связи и степень.
5)Объединение куч (union)
```
def union(self, other_heap):
    new_heap = BinomialHeap()
    new_heap.head = self.merge_roots(self.head, other_heap.head)
```
Сначала объединяет списки корней (merge_roots).
Затем проходит по результату, объединяет деревья одинаковой степени.
6)Вставка элемента (insert)
```
def insert(self, key):
    new_node = BinomialNode(key)
    new_heap = BinomialHeap()
    new_heap.head = new_node
    self.head = self.union(new_heap).head
```
Создаёт новый узел и "кучу" из одного элемента, а затем объединяет с основной кучей.
7)Поиск минимума (find_min)
```
def find_min(self):
    while x is not None:
        if x.key < min_key:
            min_key = x.key
            y = x
        x = x.sibling
    return y.key
```
Просто проходит по всем корням — выбирает минимальный key.
8)Извлечение (удаление) минимума (extract_min)
```
def extract_min(self):
    ...
    # Поиск min_node
    while x is not None:
        if x.key < min_key:
            min_key = x.key
            min_prev = prev_x
            min_node = x
        prev_x = x
        x = x.sibling
    # Удаление min_node
    ...
    # Переворачивание дочерних поддеревьев и создание новой кучи
    ...
    # Объединение с основной кучей
    ...
    return min_key
```
Находит минимум среди корней,
Удаляет этот корень из списка,
Переворачивает его поддеревья и делает из них новую кучу,
Объединяет её с основной кучей,
Возвращает значение минимального элемента.
		Куча Фибоначчи
	Определение 
Куча Фибоначчи — это структура данных, представляющая собой набор деревьев, упорядоченных по свойству неубывающей пирамиды (min-heap property), где ключ каждого узла не меньше ключа его родительского узла. Эта структура реализует абстрактный тип данных "очередь с приоритетом" и позволяет выполнять операции вставки, поиска минимального элемента и уменьшения ключа с амортизированным временем работы O(1), а операцию удаления минимального элемента — за O(logn). Основное преимущество кучи Фибоначчи — высокая эффективность операций с приоритетами благодаря ленивой структуре и особенному способу организации деревьев и связей между узлами.
	Анализ кода 
1) Класс Node
```
class Node:
    def __init__(self, key):
        self.key = key
        self.degree = 0
        self.parent = None
        self.child = None
        self.left = self
        self.right = self
        self.mark = False
```
Эта часть определяет структуру узла дерева — каждый node хранит ключ (key) и указатели на родителя (parent), ребёнка (child), соседей слева и справа (left, right), степень вершины (degree), а также метку (mark) для каскадного удаления.
Операторы self.left = self, self.right = self нужны для быстрой вставки в двусвязный список (корневой список или список детей).
2) Класс FibonacciHeap
```
class FibonacciHeap:
    def __init__(self):
        self.min = None
        self.count = 0
```
Здесь определяются поля кучи: min — указатель на вершину с минимальным ключом; count — текущее количество элементов.
3) Вставка элемента (метод insert)
```
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
```
Создаётся новый узел (node = Node(key)).
Если куча пуста (if self.min is None), новый узел становится минимальным.
Иначе он вставляется в корневой двусвязный список относительно self.min (связи left и right корректируются вручную).
Если новый ключ меньше текущего минимального, self.min обновляется на этот элемент.
4) Извлечение минимума (метод extract_min):
```
def extract_min(self):
    z = self.min
    if z is not None:
        ...
        if z.child is not None:
            ...
        # Удаление z из корневого списка
        z.left.right = z.right
        z.right.left = z.left
        ...
        if z == z.right:
            self.min = None
        else:
            self.min = z.right
            self._consolidate()
        self.count -= 1
    return z.key if z else None
```
Запоминает текущий минимальный элемент (z = self.min).
Если у элемента есть дети, добавляет их в корневой список (итерация по потомкам, разрыв связей родительства).
Удаляет узел z из корневого списка (строки z.left.right = z.right и z.right.left = z.left).
Если z был единственным элементом, куча становится пустой.
Если остались корни, вызывает консолидатор (self._consolidate()) для объединения деревьев одинаковой степени.
Возвращает ключ удалённого минимума (return z.key if z else None).
5) Консолидация (метод _consolidate):
```
def _consolidate(self):
    max_degree = 50
    A = [None] * max_degree
    ...
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
        ...
        for i in range(max_degree):
            if A[i] is not None:
                if self.min is None or A[i].key < self.min.key:
                    self.min = A[i]
```
Использует массив A для хранения деревьев по степеням.
Перебирает все корни; если встречаются деревья с одной степенью, объединяет (через _link) их в одно дерево с увеличенной степенью.
По завершению в массиве остаются только по одному дереву каждой степени; устанавливается новый минимум.
6) Уменьшение ключа (метод decrease_key):
```
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
```
Проверяет, что новый ключ меньше текущего (if k > x.key: ...).
Если новый ключ нарушает свойство кучи (стал меньше родителя), происходит отделение дочернего узла от родителя методом _cut, после чего может произойти каскадное отделение через _cascading_cut.
Если ключ стал меньше текущего минимума — обновляется self.min.
7) Вспомогательные методы: _cut, _cascading_cut, _link
_cut: Извлекает x из списка детей y, вставляет x в корневой список.
_cascading_cut: Если родитель уже был отмечен (mark == True), рекурсивно "убегает" вверх.
_link: Делает y дочерним по отношению к x (используется при слиянии в консолидаторе).
```
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
```
8. Прочее
Метод find_min просто возвращает текущий минимум:
```
def find_min(self):
    return self.min.key if self.min else N
```
		Хеш таблица
	Определение 
Хеш-таблица — это структура данных, реализующая интерфейс ассоциативного массива, которая хранит пары ключ-значение и позволяет эффективно выполнять операции добавления, удаления и поиска данных по ключу. При работе с хеш-таблицей ключ преобразуется в индекс массива с помощью хеш-функции, что обеспечивает быстрый доступ к элементам обычно за время O(1). При этом важной задачей является разрешение коллизий, когда разные ключи имеют одинаковый хеш-индекс. 
	Алгоритм кода 
1)Создание класса и инициализация:
```
class HashTable:
    def __init__(self, size=10):
        self.size = size
        self.table = [[] for _ in range(size)]
```
Создаётся класс HashTable с конструктором __init__, который принимает размер таблицы (size, по умолчанию 10).
self.table — это список из списков ([[] for _ in range(size)]), где каждая ячейка будет содержать список пар (ключ, значение) — это реализация разрешения коллизий методом цепочек.
2)Хеш-функция:
```
def _hash(self, key):
    return hash(key) % self.size
```
Внутренний метод _hash вычисляет индекс для ключа: берет стандартную функцию hash(key) и остаток от деления на размер таблицы (% self.size). Это определяет "корзину", в которую попадёт элемент.
3)Добавление элемента (put):
```
def put(self, key, value):
    index = self._hash(key)
    for i, (k, v) in enumerate(self.table[index]):
        if k == key:
            self.table[index][i] = (key, value)
            return
    self.table[index].append((key, value))
```
Находим индекс с помощью _hash.
Проходим по элементам в этой корзине (for i, (k, v) in enumerate(self.table[index]):). Если ключ уже есть (if k == key:), то обновляем значение (self.table[index][i] = (key, value)).
Если ключ не найден, добавляем новый элемент через append.
4)Получение значения (get):
```
def get(self, key):
    index = self._hash(key)
    for k, v in self.table[index]:
        if k == key:
            return v
    return None
```
Снова вычисляем индекс корзины.
Перебираем все пары в корзине. Если ключ найден — возвращаем значение (return v).
Если ключа нет — возвращается None.
5)Удаление элемента (remove):
```
def remove(self, key):
    index = self._hash(key)
    for i, (k, v) in enumerate(self.table[index]):
        if k == key:
            del self.table[index][i]
            return True
    return False
```
Получаем индекс хеш-таблицы.
Ищем ключ в списке, если находим — удаляем (del self.table[index][i]) и возвращаем True.
Если не находим — возвращаем False.
6)Использование:
```
ht = HashTable()
ht.put("apple", 10)
ht.put("banana", 20)
print(ht.get("apple"))   # 10
print(ht.get("banana"))  # 20
ht.remove("apple")
print(ht.get("apple"))   # None
```
Создаём объект ht.
Добавляем пары ключ-значение через put.
Извлекаем значения через get.
Удаляем ключ через remove.