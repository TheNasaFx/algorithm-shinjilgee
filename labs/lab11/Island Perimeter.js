function islandPerimeter(grid) {
  const rows = grid.length;
  const cols = grid[0].length;
  let perimeter = 0;

  for (let i = 0; i < rows; i++) {
      for (let j = 0; j < cols; j++) {
          if (grid[i][j] === 1) { // Land cell
              perimeter += 4; // Each land cell contributes 4 to the perimeter

              // Check for adjacent land cells to reduce the perimeter
              if (i > 0 && grid[i - 1][j] === 1) perimeter -= 1; // Cell above
              if (i < rows - 1 && grid[i + 1][j] === 1) perimeter -= 1; // Cell below
              if (j > 0 && grid[i][j - 1] === 1) perimeter -= 1; // Cell to the left
              if (j < cols - 1 && grid[i][j + 1] === 1) perimeter -= 1; // Cell to the right
          }
      }
  }

  return perimeter;
}

// Examples
console.log(islandPerimeter([
  [0, 1, 0, 0],
  [1, 1, 1, 0],
  [0, 1, 0, 0],
  [1, 1, 0, 0]
])); // Output: 16

console.log(islandPerimeter([[1]])); // Output: 4

console.log(islandPerimeter([[1, 0]])); // Output: 4
