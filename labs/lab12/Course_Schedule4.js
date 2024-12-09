/**
 * @param {number} numCourses
 * @param {number[][]} prerequisites
 * @param {number[][]} queries
 * @return {boolean[]}
 */
function checkIfPrerequisite(numCourses, prerequisites, queries) {
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

  return queries.map(([u, v]) => isPrerequisite[u][v]);
}

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
