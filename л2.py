#Пример создания мультисписка (вложенного списка):
groups = [['Артемий', 'Тимур'], ['Уля', 'Аля'], ['Артем', 'Даня']]


#Пример создания очереди:
from queue import Queue
q = Queue()
q.put(1) 
q.put(2) 
q.put(3)


#Пример реализации дека:
from collections import deque
tasks = deque() 
tasks.append("task1")
tasks.append("task2")
tasks.append("task3") 

#Пр
имер реализации приоритетной очереди:
from queue import PriorityQueue 
q = PriorityQueue()
q.put((2, 'mid-priority item')) 
q.put((1, 'high-priority item')) 
q.put((3, 'low-priority item')) 


#Пример приоритетной очереди с использованием бинарной кучи:
import heapq   
heapq.heappush(customers, (2, "Женя")) 
heapq.heappush(customers, (3, "Захар")) 
heapq.heappush(customers, (1, "Надя")) 
heapq.heappush(customers, (4, "Соня")) 
