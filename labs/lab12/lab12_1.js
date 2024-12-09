function topologicalSortDFS(vertices, edges) {
  const graph = Array.from({ length: vertices }, () => []);
  edges.forEach(([u, v]) => graph[u].push(v));

  const visited = new Set();
  const stack = [];

  function dfs(node) {
    if (!visited.has(node)) {
      visited.add(node);
      graph[node].forEach((neighbor) => dfs(neighbor));
      stack.push(node);
    }
  }

  for (let vertex = 0; vertex < vertices; vertex++) {
    if (!visited.has(vertex)) {
      dfs(vertex);
    }
  }

  return stack.reverse();
}

// Example Usage:
const V = 6;
const E = [
  [2, 3],
  [3, 1],
  [4, 0],
  [4, 1],
  [5, 0],
  [5, 2],
];
const result = topologicalSortDFS(V, E);
console.log("Topological Order:", result);
