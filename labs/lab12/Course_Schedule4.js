/**
 * @param {number} numCourses
 * @param {number[][]} prerequisites
 * @param {number[][]} queries
 * @return {boolean[]}
 */
function checkIfPrerequisite(numCourses, prerequisites, queries) {
  // Step 1: Initialize the graph and transitive closure matrix
  const graph = new Map();
  for (let i = 0; i < numCourses; i++) {
    graph.set(i, []);
  }
  for (const [a, b] of prerequisites) {
    graph.get(a).push(b);
  }

  const isPrerequisite = Array.from({ length: numCourses }, () =>
    Array(numCourses).fill(false)
  );

  // Step 2: Perform DFS to fill transitive closure
  function dfs(course, target) {
    if (isPrerequisite[course][target]) return;
    isPrerequisite[course][target] = true;
    for (const neighbor of graph.get(target)) {
      dfs(course, neighbor);
    }
  }

  for (let course = 0; course < numCourses; course++) {
    for (const neighbor of graph.get(course)) {
      dfs(course, neighbor);
    }
  }

  // Step 3: Answer the queries
  return queries.map(([u, v]) => isPrerequisite[u][v]);
}

// Example usage
console.log(
  checkIfPrerequisite(
    2,
    [[1, 0]],
    [
      [0, 1],
      [1, 0],
    ]
  )
); // Output: [false, true]
console.log(
  checkIfPrerequisite(
    2,
    [],
    [
      [1, 0],
      [0, 1],
    ]
  )
); // Output: [false, false]
console.log(
  checkIfPrerequisite(
    3,
    [
      [1, 2],
      [1, 0],
      [2, 0],
    ],
    [
      [1, 0],
      [1, 2],
    ]
  )
); // Output: [true, true]
