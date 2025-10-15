# Через list comprehension для создания вложенного списка имён
names1 = ['Артемий', 'Тимур']
names2 = ['Артем', 'Даня']
names3 = ['Захар', 'Ежик']
groups = [names1, names2, names3]


# очередь 
from collections import deque

q = deque()
for i in range(1, 4):
    q.append(i)

while q:
    print(q.popleft())  # FIFO-поведение


#ДЕК 

from collections import deque

tasks = deque(["task1", "task2", "task3"])
tasks.appendleft("urgent_task")
while tasks:
    print(tasks.pop())  # LIFO-поведение (pop с конца)


# Приоритетная очередь через heapq
import heapq

tasks = []
heapq.heappush(tasks, (2, "mid-priority item"))
heapq.heappush(tasks, (1, "high-priority item"))
heapq.heappush(tasks, (3, "low-priority item"))


import heapq

# приоритетная очередь с использованием бинарной кучи
priority_queue = []

heapq.heappush(priority_queue, (2, 'Задача средней важности'))
heapq.heappush(priority_queue, (1, 'Срочная задача'))
heapq.heappush(priority_queue, (3, 'Обычная задача'))
heapq.heappush(priority_queue, (4, 'Малозначимая задача'))

while priority_queue:
    priority, task = heapq.heappop(priority_queue)
    print(f'Выполняется: {task} с приоритетом {priority}')
