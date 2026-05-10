# dfs.py

graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

def dfs(graph, start, goal, path=[]):
    path = path + [start]

    if start == goal:
        return path

    for neighbor in graph[start]:
        if neighbor not in path:
            new_path = dfs(graph, neighbor, goal, path)

            if new_path:
                return new_path

    return None

path = dfs(graph, 'A', 'F')

print("DFS Path:", path)  