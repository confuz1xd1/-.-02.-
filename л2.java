import java.util.*;

public class Main {
    public static void main(String[] args) {
        // 1. Вложенные списки ("группы")
        List<String> names1 = Arrays.asList("Артемий", "Тимур");
        List<String> names2 = Arrays.asList("Артем", "Даня");
        List<String> names3 = Arrays.asList("Захар", "Ежик");
        List<List<String>> groups = Arrays.asList(names1, names2, names3);

        for (List<String> group : groups) {
            for (String name : group) {
                System.out.print(name + " ");
            }
            System.out.println();
        }

        // 2. Очередь (FIFO)
        Queue<Integer> q = new LinkedList<>();
        for (int i = 1; i < 4; i++) {
            q.add(i);
        }
        while (!q.isEmpty()) {
            System.out.println(q.poll()); // FIFO поведение
        }

        // 3. Двусторонняя очередь (дек)
        Deque<String> tasks = new LinkedList<>(Arrays.asList("task1", "task2", "task3"));
        tasks.addFirst("urgent_task");
        while (!tasks.isEmpty()) {
            System.out.println(tasks.removeLast()); // LIFO поведение (с конца)
        }

        // 4. Приоритетная очередь (min heap)
        PriorityQueue<Task> pq = new PriorityQueue<>();
        pq.add(new Task(2, "mid-priority item"));
        pq.add(new Task(1, "high-priority item"));
        pq.add(new Task(3, "low-priority item"));

        while (!pq.isEmpty()) {
            Task t = pq.poll();
            System.out.println("Выполняется: " + t.name + " с приоритетом " + t.priority);
        }

        // 5. Приоритетная очередь с русскими задачами (min heap)
        PriorityQueue<Task> priorityQueue = new PriorityQueue<>();
        priorityQueue.add(new Task(2, "Задача средней важности"));
        priorityQueue.add(new Task(1, "Срочная задача"));
        priorityQueue.add(new Task(3, "Обычная задача"));
        priorityQueue.add(new Task(4, "Малозначимая задача"));

        while (!priorityQueue.isEmpty()) {
            Task t = priorityQueue.poll();
            System.out.println("Выполняется: " + t.name + " с приоритетом " + t.priority);
        }
    }

    // Вспомогательный класс для задач
    static class Task implements Comparable<Task> {
        int priority;
        String name;

        Task(int priority, String name) {
            this.priority = priority;
            this.name = name;
        }

        @Override
        public int compareTo(Task other) {
            return Integer.compare(this.priority, other.priority);
        }
    }
}
