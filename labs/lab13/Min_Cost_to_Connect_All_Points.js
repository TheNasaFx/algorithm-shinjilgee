class MinHeap {
  constructor() {
    this.heap = [];
  }

  // Push an element to the heap
  add([cost, point]) {
    this.heap.push([cost, point]);
    this.heapifyUp();
  }

  // Remove and return the minimum element (root of the heap)
  remove() {
    if (this.heap.length === 1) {
      return this.heap.pop();
    }

    const min = this.heap[0];
    this.heap[0] = this.heap.pop();
    this.heapifyDown();
    return min;
  }

  // Restore the heap property from bottom to top
  heapifyUp() {
    let index = this.heap.length - 1;
    while (index > 0) {
      const parentIndex = Math.floor((index - 1) / 2);
      if (this.heap[parentIndex][0] <= this.heap[index][0]) break;
      [this.heap[parentIndex], this.heap[index]] = [
        this.heap[index],
        this.heap[parentIndex],
      ];
      index = parentIndex;
    }
  }

  // Restore the heap property from top to bottom
  heapifyDown() {
    let index = 0;
    const length = this.heap.length;
    while (index < length) {
      let leftChildIndex = 2 * index + 1;
      let rightChildIndex = 2 * index + 2;
      let smallest = index;

      if (
        leftChildIndex < length &&
        this.heap[leftChildIndex][0] < this.heap[smallest][0]
      ) {
        smallest = leftChildIndex;
      }
      if (
        rightChildIndex < length &&
        this.heap[rightChildIndex][0] < this.heap[smallest][0]
      ) {
        smallest = rightChildIndex;
      }
      if (smallest === index) break;
      [this.heap[index], this.heap[smallest]] = [
        this.heap[smallest],
        this.heap[index],
      ];
      index = smallest;
    }
  }
}

/**
 * @param {number[][]} points
 * @return {number}
 */
var minCostConnectPoints = function (points) {
  const n = points.length;
  const visited = Array(n).fill(false); // Array to keep track of visited points
  const minHeap = new MinHeap(); // Min-heap to store the edges (cost, point index)
  let totalCost = 0;
  let edgesUsed = 0;

  // Function to calculate the Manhattan distance between two points
  const manhattanDistance = (p1, p2) => {
    return Math.abs(p1[0] - p2[0]) + Math.abs(p1[1] - p2[1]);
  };

  // Start from the first point (index 0)
  visited[0] = true;

  // Add edges from point 0 to the heap
  for (let i = 1; i < n; i++) {
    const cost = manhattanDistance(points[0], points[i]);
    minHeap.add([cost, i]);
  }

  // Prim's Algorithm to find MST
  while (edgesUsed < n - 1) {
    // Get the edge with the minimum cost
    const [cost, point] = minHeap.remove();

    // Skip if the point is already visited
    if (visited[point]) {
      continue;
    }

    // Add the cost of this edge to the total cost and mark the point as visited
    visited[point] = true;
    totalCost += cost;
    edgesUsed++;

    // Add new edges from the current point to the heap
    for (let i = 0; i < n; i++) {
      if (!visited[i]) {
        const newCost = manhattanDistance(points[point], points[i]);
        minHeap.add([newCost, i]);
      }
    }
  }

  return totalCost;
};

// Example usage
console.log(
  minCostConnectPoints([
    [0, 0],
    [2, 2],
    [3, 10],
    [5, 2],
    [7, 0],
  ])
); // Output: 20
console.log(
  minCostConnectPoints([
    [3, 12],
    [-2, 5],
    [-4, 1],
  ])
); // Output: 18
