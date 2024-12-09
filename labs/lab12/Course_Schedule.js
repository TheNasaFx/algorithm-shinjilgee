/**
 * @param {number} numCourses
 * @param {number[][]} prerequisites
 * @return {boolean}
 */
function canFinish(numCourses, prerequisites) {
  // Step 1: Build the graph and in-degree array
  const graph = new Map(); // Adjacency list representation
  const inDegree = Array(numCourses).fill(0); // Array to track the number of prerequisites

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

  // Step 3: Process courses
  let processedCourses = 0;

  while (queue.length > 0) {
    const current = queue.shift();
    processedCourses++;

    // Reduce in-degree of neighbors and add to queue if in-degree becomes 0
    if (graph.has(current)) {
      for (const neighbor of graph.get(current)) {
        inDegree[neighbor]--;
        if (inDegree[neighbor] === 0) queue.push(neighbor);
      }
    }
  }

  // Step 4: Check if all courses have been processed
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
