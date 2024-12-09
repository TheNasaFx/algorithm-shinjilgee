/**
 * @param {number} numCourses
 * @param {number[][]} prerequisites
 * @return {number[]}
 */
function findOrder(numCourses, prerequisites) {
  // Step 1: Build the graph and in-degree array
  const graph = new Map();
  const inDegree = Array(numCourses).fill(0);

  for (const [course, pre] of prerequisites) {
    if (!graph.has(pre)) graph.set(pre, []);
    graph.get(pre).push(course);
    inDegree[course]++;
  }

  // Step 2: Initialize the queue with courses that have no prerequisites
  const queue = [];
  for (let i = 0; i < numCourses; i++) {
    if (inDegree[i] === 0) queue.push(i);
  }

  const courseOrder = [];

  // Step 3: Process the courses
  while (queue.length > 0) {
    const current = queue.shift();
    courseOrder.push(current);

    if (graph.has(current)) {
      for (const neighbor of graph.get(current)) {
        inDegree[neighbor]--;
        if (inDegree[neighbor] === 0) {
          queue.push(neighbor);
        }
      }
    }
  }

  // Step 4: Check if all courses are processed
  return courseOrder.length === numCourses ? courseOrder : [];
}

// Example usage
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
