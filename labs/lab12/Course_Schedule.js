/**
 * @param {number} numCourses
 * @param {number[][]} prerequisites
 * @return {boolean}
 */
function canFinish(numCourses, prerequisites) {
  const graph = new Map();
  const inDegree = Array(numCourses).fill(0);

  for (const [course, pre] of prerequisites) {
    if (!graph.has(pre)) graph.set(pre, []);
    graph.get(pre).push(course);
    inDegree[course]++;
  }

  const queue = [];
  for (let i = 0; i < numCourses; i++) {
    if (inDegree[i] === 0) queue.push(i);
  }

  let processedCourses = 0;

  while (queue.length > 0) {
    const current = queue.shift();
    processedCourses++;

    if (graph.has(current)) {
      for (const neighbor of graph.get(current)) {
        inDegree[neighbor]--;
        if (inDegree[neighbor] === 0) queue.push(neighbor);
      }
    }
  }

  return processedCourses === numCourses;
}

// Example usage
console.log(canFinish(2, [[1, 0]])); // Output: true
console.log(
  canFinish(2, [
    [1, 0],
    [0, 1],
  ])
); // Output: false
