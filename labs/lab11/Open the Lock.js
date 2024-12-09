function openLock(deadends, target) {
  const deadSet = new Set(deadends);
  const visited = new Set();
  const queue = [["0000", 0]];

  if (deadSet.has("0000")) return -1;

  while (queue.length > 0) {
    const [combination, steps] = queue.shift();

    if (combination === target) return steps;

    if (visited.has(combination) || deadSet.has(combination)) continue;

    visited.add(combination);

    for (let i = 0; i < 4; i++) {
      const digit = parseInt(combination[i]);
      for (const move of [-1, 1]) {
        // Move the wheel up or down
        const newDigit = (digit + move + 10) % 10;
        const newCombination =
          combination.slice(0, i) + newDigit + combination.slice(i + 1);

        if (!visited.has(newCombination) && !deadSet.has(newCombination)) {
          queue.push([newCombination, steps + 1]);
        }
      }
    }
  }

  return -1;
}

// Examples
console.log(openLock(["0201", "0101", "0102", "1212", "2002"], "0202")); // Output: 6
console.log(openLock(["8888"], "0009")); // Output: 1
console.log(
  openLock(
    ["8887", "8889", "8878", "8898", "8788", "8988", "7888", "9888"],
    "8888"
  )
); // Output: -1
