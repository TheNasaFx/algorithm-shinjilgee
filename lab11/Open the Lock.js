/**
 * @param {string[]} deadends
 * @param {string} target
 * @return {number}
 */
function openLock(deadends, target) {
  const dead = new Set(deadends);
  if (dead.has("0000")) {
    return -1;
  }

  const queue = [["0000", 0]];
  const visited = new Set(["0000"]);

  while (queue.length > 0) {
    const [current, turns] = queue.shift();

    if (current === target) {
      return turns;
    }

    for (let i = 0; i < 4; i++) {
      const digit = parseInt(current[i]);
      for (let move of [-1, 1]) {
        const nextDigit = (digit + move + 10) % 10;
        const nextCombination =
          current.slice(0, i) + nextDigit + current.slice(i + 1);

        if (!visited.has(nextCombination) && !dead.has(nextCombination)) {
          visited.add(nextCombination);
          queue.push([nextCombination, turns + 1]);
        }
      }
    }
  }

  return -1;
}

console.log(openLock(["0201", "0101", "0102", "1212", "2002"], "0202")); // Output: 6
console.log(openLock(["8888"], "0009")); // Output: 1
console.log(
  openLock(
    ["8887", "8889", "8878", "8898", "8788", "8988", "7888", "9888"],
    "8888"
  )
); // Output: -1
