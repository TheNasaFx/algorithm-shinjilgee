def topological_sort_dfs(vertices, edges):
    from collections import defaultdict
    
    graph = defaultdict(list)
    for u, v in edges:
        graph[u].append(v)

    visited = set()
    stack = []

    def dfs(node):
        if node not in visited:
            visited.add(node)
            for neighbor in graph[node]:
                dfs(neighbor)
            stack.append(node)

    for vertex in range(vertices):
        if vertex not in visited:
            dfs(vertex)

    return stack[::-1]  

# Example Usage:
V = 6
E = [[2, 3], [3, 1], [4, 0], [4, 1], [5, 0], [5, 2]]
result = topological_sort_dfs(V, E)
print("Topological Order:", result)
