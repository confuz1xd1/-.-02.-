code3 Java

import java.util.ArrayList;

public class BinaryHeap {
    private ArrayList<Integer> heap = new ArrayList<>();

    private int parent(int i) { return (i - 1) / 2; }
    private int leftChild(int i) { return 2 * i + 1; }
    private int rightChild(int i) { return 2 * i + 2; }

    private void siftUp(int i) {
        while (i > 0 && heap.get(parent(i)) < heap.get(i)) {
            // Меняем местами
            int temp = heap.get(i);
            heap.set(i, heap.get(parent(i)));
            heap.set(parent(i), temp);
            i = parent(i);
        }
    }

    private void siftDown(int i) {
        int maxIndex = i;
        int left = leftChild(i);
        int right = rightChild(i);

        if (left < heap.size() && heap.get(left) > heap.get(maxIndex))
            maxIndex = left;
        if (right < heap.size() && heap.get(right) > heap.get(maxIndex))
            maxIndex = right;
        if (maxIndex != i) {
            int temp = heap.get(i);
            heap.set(i, heap.get(maxIndex));
            heap.set(maxIndex, temp);
            siftDown(maxIndex);
        }
    }

    public void insert(int key) {
        heap.add(key);
        siftUp(heap.size() - 1);
    }

    public Integer extractMax() {
        if (heap.isEmpty()) return null;
        if (heap.size() == 1) return heap.remove(0);

        int result = heap.get(0);
        heap.set(0, heap.remove(heap.size() - 1));
        siftDown(0);
        return result;
    }

    public Integer getMax() {
        if (heap.isEmpty()) return null;
        return heap.get(0);
    }

    public int size() {
        return heap.size();
    }

    // Пример использования:
    public static void main(String[] args) {
        BinaryHeap bh = new BinaryHeap();
        bh.insert(10);
        bh.insert(20);
        bh.insert(5);

        System.out.println("Максимальный элемент: " + bh.getMax());        // 20
        System.out.println("Извлечь максимум: " + bh.extractMax());        // 20
        System.out.println("Максимальный элемент после извлечения: " + bh.getMax()); // 10
    }
}

class BinomialNode {
    int key;
    int degree;
    BinomialNode parent, child, sibling;

    BinomialNode(int key) {
        this.key = key;
        this.degree = 0;
        this.parent = null;
        this.child = null;
        this.sibling = null;
    }
}

class BinomialHeap {
    BinomialNode head;

    BinomialHeap() {
        this.head = null;
    }

    private BinomialNode mergeRoots(BinomialNode h1, BinomialNode h2) {
        if (h1 == null) return h2;
        if (h2 == null) return h1;
        if (h1.degree <= h2.degree) {
            h1.sibling = mergeRoots(h1.sibling, h2);
            return h1;
        } else {
            h2.sibling = mergeRoots(h1, h2.sibling);
            return h2;
        }
    }

    private void link(BinomialNode y, BinomialNode z) {
        y.parent = z;
        y.sibling = z.child;
        z.child = y;
        z.degree++;
    }

    private BinomialNode unionHeaps(BinomialNode h1, BinomialNode h2) {
        BinomialNode newHead = mergeRoots(h1, h2);
        if (newHead == null) return null;

        BinomialNode prev = null;
        BinomialNode curr = newHead;
        BinomialNode next = curr.sibling;

        while (next != null) {
            if (curr.degree != next.degree ||
                (next.sibling != null && next.sibling.degree == curr.degree)) {
                prev = curr;
                curr = next;
            } else {
                if (curr.key <= next.key) {
                    curr.sibling = next.sibling;
                    link(next, curr);
                } else {
                    if (prev != null) prev.sibling = next;
                    else newHead = next;
                    link(curr, next);
                    curr = next;
                }
            }
            next = curr.sibling;
        }
        return newHead;
    }

    public void insert(int key) {
        BinomialNode node = new BinomialNode(key);
        BinomialHeap temp = new BinomialHeap();
        temp.head = node;
        this.head = unionHeaps(this.head, temp.head);
    }

    public int findMin() {
        if (head == null) return Integer.MAX_VALUE;
        int minKey = Integer.MAX_VALUE;
        BinomialNode curr = head;
        while (curr != null) {
            if (curr.key < minKey)
                minKey = curr.key;
            curr = curr.sibling;
        }
        return minKey;
    }

    public int extractMin() {
        if (head == null) return Integer.MAX_VALUE;
        BinomialNode minNode = head;
        BinomialNode minPrev = null;
        BinomialNode prev = null;
        BinomialNode curr = head;
        int minKey = curr.key;

        while (curr != null) {
            if (curr.key < minKey) {
                minKey = curr.key;
                minNode = curr;
                minPrev = prev;
            }
            prev = curr;
            curr = curr.sibling;
        }

        // Remove minNode from root list
        if (minPrev != null)
            minPrev.sibling = minNode.sibling;
        else
            head = minNode.sibling;

        // Reverse minNode's children
        BinomialNode child = minNode.child;
        BinomialNode revChild = null;
        while (child != null) {
            BinomialNode next = child.sibling;
            child.parent = null;
            child.sibling = revChild;
            revChild = child;
            child = next;
        }
        head = unionHeaps(head, revChild);
        return minKey;
    }

    // Пример использования
    public static void main(String[] args) {
        BinomialHeap bh = new BinomialHeap();
        bh.insert(10);
        bh.insert(3);
        bh.insert(8);
        bh.insert(21);
        bh.insert(14);

        System.out.println("Минимальный элемент: " + bh.findMin());
        System.out.println("Удалён минимальный элемент: " + bh.extractMin());
        System.out.println("Новый минимальный элемент: " + bh.findMin());
    }
}

==========================================================================================

Куча Фибоначчи

class Node {
    int key;
    int degree;
    boolean mark;
    Node parent;
    Node child;
    Node left;
    Node right;

    public Node(int key) {
        this.key = key;
        this.degree = 0;
        this.mark = false;
        this.parent = null;
        this.child = null;
        this.left = this;
        this.right = this;
    }
}

public class FibonacciHeap {
    private Node min;
    private int count;

    public FibonacciHeap() {
        min = null;
        count = 0;
    }

    public Node insert(int key) {
        Node node = new Node(key);
        if (min == null) {
            min = node;
        } else {
            // Вставка в корневой список
            node.left = min;
            node.right = min.right;
            min.right.left = node;
            min.right = node;
            if (key < min.key) min = node;
        }
        count++;
        return node;
    }

    public void merge(FibonacciHeap other) {
        if (other.min == null) return;
        if (min == null) {
            min = other.min;
            count = other.count;
            return;
        }
        min.right.left = other.min.left;
        other.min.left.right = min.right;
        min.right = other.min;
        other.min.left = min;
        if (other.min.key < min.key) min = other.min;
        count += other.count;
    }

    public int extractMin() {
        Node z = min;
        if (z == null) return Integer.MAX_VALUE;
        // Переносим детей z в корневой список
        if (z.child != null) {
            Node child = z.child;
            do {
                Node next = child.right;
                child.parent = null;
                // Вставка в корневой список
                child.left = min;
                child.right = min.right;
                min.right.left = child;
                min.right = child;
                child = next;
            } while (child != z.child);
        }
        // Удаляем z из корневого списка
        z.left.right = z.right;
        z.right.left = z.left;
        if (z == z.right) {
            min = null;
        } else {
            min = z.right;
            consolidate();
        }
        count--;
        return z.key;
    }

    public void decreaseKey(Node x, int k) {
        if (k > x.key) throw new IllegalArgumentException("new key is greater than current key");
        x.key = k;
        Node y = x.parent;
        if (y != null && x.key < y.key) {
            cut(x, y);
            cascadingCut(y);
        }
        if (x.key < min.key) min = x;
    }

    public int findMin() {
        return min == null ? Integer.MAX_VALUE : min.key;
    }

    private void consolidate() {
        int maxDegree = 50;
        Node[] A = new Node[maxDegree];
        Node x = min;
        if (x == null) return;
        Node start = x;
        do {
            Node w = x;
            int d = w.degree;
            while (A[d] != null) {
                Node y = A[d];
                if (w.key > y.key) {
                    Node temp = w; w = y; y = temp;
                }
                link(y, w);
                A[d] = null;
                d++;
            }
            A[d] = w;
            x = x.right;
        } while (x != start);
        min = null;
        for (Node node : A) {
            if (node != null) {
                if (min == null || node.key < min.key)
                    min = node;
            }
        }
    }

    private void link(Node y, Node x) {
        // Удаляем y из корневого списка
        y.left.right = y.right;
        y.right.left = y.left;
        y.parent = x;
        if (x.child == null) {
            x.child = y;
            y.left = y;
            y.right = y;
        } else {
            y.left = x.child;
            y.right = x.child.right;
            x.child.right.left = y;
            x.child.right = y;
        }
        x.degree++;
        y.mark = false;
    }

    private void cut(Node x, Node y) {
        if (x.right == x) {
            y.child = null; // <--- Эта строка для отделения, если x был единственным ребёнком.
        } else if (y.child == x) {
            y.child = x.right;
        }
        x.left.right = x.right;
        x.right.left = x.left;
        y.degree--;
        // Добавляем x в корневой список
        x.left = min;
        x.right = min.right;
        min.right.left = x;
        min.right = x;
        x.parent = null;
        x.mark = false;
    }

    private void cascadingCut(Node y) {
        Node z = y.parent;
        if (z != null) {
            if (!y.mark) {
                y.mark = true;
            } else {
                cut(y, z);
                cascadingCut(z);
            }
        }
    }
}

==========================================================================================

Хеш таблица

import java.util.ArrayList;
import java.util.LinkedList;

class HashTable {
    private int size;
    private ArrayList<LinkedList<Entry>> table;

    // Внутренний класс для хранения пары ключ-значение
    static class Entry {
        String key;
        int value;

        Entry(String key, int value) {
            this.key = key;
            this.value = value;
        }
    }

    public HashTable(int size) {
        this.size = size;
        table = new ArrayList<>(size);
        for (int i = 0; i < size; i++) {
            table.add(new LinkedList<>());
        }
    }

    private int hash(String key) {
        // Стандартная хеш-функция и остаток по размеру таблицы
        return Math.abs(key.hashCode()) % size;
    }

    public void put(String key, int value) {
        int idx = hash(key);
        LinkedList<Entry> bucket = table.get(idx);
        for (Entry entry : bucket) {
            if (entry.key.equals(key)) {
                entry.value = value; // Обновление значения
                return;
            }
        }
        bucket.add(new Entry(key, value)); // Добавление новой пары
    }

    public Integer get(String key) {
        int idx = hash(key);
        LinkedList<Entry> bucket = table.get(idx);
        for (Entry entry : bucket) {
            if (entry.key.equals(key)) {
                return entry.value;
            }
        }
        return null; // Если ключ не найден
    }

    public boolean remove(String key) {
        int idx = hash(key);
        LinkedList<Entry> bucket = table.get(idx);
        for (Entry entry : bucket) {
            if (entry.key.equals(key)) {
                bucket.remove(entry);
                return true;
            }
        }
        return false; // Если ключ не найден
    }
    
    // Пример использования
    public static void main(String[] args) {
        HashTable ht = new HashTable(10);

        ht.put("apple", 10);
        ht.put("banana", 20);

        System.out.println(ht.get("apple"));   // Выведет 10
        System.out.println(ht.get("banana"));  // Выведет 20

        ht.remove("apple");
        System.out.println(ht.get("apple"));   // Выведет null
    }
}
