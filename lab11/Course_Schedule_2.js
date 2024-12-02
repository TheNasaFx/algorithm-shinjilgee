/**
 * @param {number} numCourses
 * @param {number[][]} prerequisites
 * @return {number[]}
 */
function findOrder(numCourses, prerequisites) {
  const graph = new Map();
  const inDegree = Array(numCourses).fill(0);

  for (const [course, pre] of prerequisites) {
    if (!graph.has(pre)) graph.set(pre, []);
    graph.get(pre).push(course);
    inDegree[course]++;
  }

  const queue = [];
  for (let i = 0; i < numCourses; i++) {
    if (inDegree[i] === 0) {
      queue.push(i);
    }
  }

  const order = [];

  while (queue.length > 0) {
    const course = queue.shift();
    order.push(course);

    if (graph.has(course)) {
      for (const neighbor of graph.get(course)) {
        inDegree[neighbor]--;
        if (inDegree[neighbor] === 0) {
          queue.push(neighbor);
        }
      }
    }
  }

  return order.length === numCourses ? order : [];
}

console.log(findOrder(2, [[1, 0]])); // Output: [0, 1]
console.log(
  findOrder(4, [
    [1, 0],
    [2, 0],
    [3, 1],
    [3, 2],
  ])
); // Output: [0, 1, 2, 3] or [0, 2, 1, 3]
console.log(findOrder(1, [])); // Output: [0]
