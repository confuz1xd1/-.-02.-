import numpy as np

# Пример входной матрицы расстояний
dist = np.array([
    [0, 2, 9, 10, 7],
    [2, 0, 6, 4, 3],
    [9, 6, 0, 8, 5],
    [10, 4, 8, 0, 1],
    [7, 3, 5, 1, 0]
])

# 1. MST (алгоритм Прима)
def prim_mst(graph):
    n = len(graph)
    selected = [False] * n
    selected[0] = True
    edges = []
    for _ in range(n-1):
        minimum = float('inf')
        x, y = 0, 0
        for i in range(n):
            if selected[i]:
                for j in range(n):
                    if not selected[j] and graph[i][j] and graph[i][j] < minimum:
                        minimum = graph[i][j]
                        x, y = i, j
        selected[y] = True
        edges.append((x, y))
    return edges

mst_edges = prim_mst(dist)
mst_cost = sum(dist[u][v] for u, v in mst_edges)

# 2. Удвоение рёбер
double_edges = mst_edges + [(v, u) for u, v in mst_edges]
euler_graph = np.zeros_like(dist)
for u, v in double_edges:
    euler_graph[u][v] += 1

# 3. Эйлеров обход
def dfs_euler(u, graph, visited, path):
    for v in range(len(graph)):
        while graph[u][v] > 0 and not visited[u][v]:
            graph[u][v] -= 1
            graph[v][u] -= 1
            visited[u][v] = visited[v][u] = True
            dfs_euler(v, graph, visited, path)
    path.append(u)

visited = np.zeros_like(dist, dtype=bool)
graph_copy = euler_graph.copy()
euler_path = []
dfs_euler(0, graph_copy, visited, euler_path)
euler_path = euler_path[::-1]

# 4. Гамильтонов путь (удаляем повторы)
def remove_duplicates(path):
    res = []
    used = set()
    for node in path:
        if node not in used:
            res.append(node)
            used.add(node)
    res.append(res[0])
    return res

hamiltonian_path = remove_duplicates(euler_path)
tsp_cost = sum(dist[hamiltonian_path[i]][hamiltonian_path[i+1]] for i in range(len(hamiltonian_path)-1))

# 5. Итоги
print("Маршрут TSP:", hamiltonian_path)
print("Стоимость маршрута:", tsp_cost)
print("MST стоимость:", mst_cost)
print("Отношение TSP/MST:", round(tsp_cost/mst_cost, 2))
