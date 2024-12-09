class Solution:
    def islandPerimeter(self, grid):
        rows, cols = len(grid), len(grid[0])
        visited = set()
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        def dfs(x, y):
            if x < 0 or x >= rows or y < 0 or y >= cols or grid[x][y] == 0:
                return 1
            if (x, y) in visited:
                return 0

            visited.add((x, y))
            perimeter = 0
            for dx, dy in directions:
                perimeter += dfs(x + dx, y + dy)
            return perimeter

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    return dfs(i, j)

# Example usage
if __name__ == "__main__":
    solution = Solution()
    grid = [[0, 1, 0, 0], [1, 1, 1, 0], [0, 1, 0, 0], [1, 1, 0, 0]]
    print(solution.islandPerimeter(grid))  # Output: 16
