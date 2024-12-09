function leastInterval(tasks, n) {
    const taskCounts = {};
    for (let task of tasks) {
        taskCounts[task] = (taskCounts[task] || 0) + 1;
    }

    const maxHeap = Object.values(taskCounts).sort((a, b) => b - a);
    const maxCount = maxHeap[0];
    let idleSlots = (maxCount - 1) * n;

    for (let i = 1; i < maxHeap.length; i++) {
        idleSlots -= Math.min(maxCount - 1, maxHeap[i]);
    }

    return idleSlots > 0 ? idleSlots + tasks.length : tasks.length;
}

// Example usage:
console.log(leastInterval(["A", "A", "A", "B", "B", "B"], 2));  // Output: 8
console.log(leastInterval(["A", "C", "A", "B", "D", "B"], 1));  // Output: 6
console.log(leastInterval(["A", "A", "A", "B", "B", "B"], 3));  // Output: 10
