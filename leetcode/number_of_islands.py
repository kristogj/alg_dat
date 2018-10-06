class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if not grid:
            return 0
        rows = len(grid)
        cols = len(grid[0])
        islands = 0
        for x in range(rows):
            for y in range(cols):
                if grid[x][y] == "1":
                    islands += 1
                    self.search(grid, x, y, rows, cols)
        return islands

    def search(self, grid, x, y, rows, cols):
        # BFS
        queue = [(x, y)]
        while queue:
            x, y = queue.pop(0)
            grid[x][y] = "2"
            self.append(grid,queue, x - 1, y, rows, cols)
            self.append(grid,queue, x, y + 1, rows, cols)
            self.append(grid,queue, x + 1, y, rows, cols)
            self.append(grid,queue, x, y - 1, rows, cols)

    def append(self,grid, queue, x, y, rows, cols):
        if (x >= 0 and x < rows) and (y >= 0 and y < cols):
            if grid[x][y] == "1":
                queue.append((x, y))


print(Solution().numIslands([["1","1","1","1","1","0","1","1","1","1","1","1","1","1","1","0","1","0","1","1"],
                             ["0","1","1","1","1","1","1","1","1","1","1","1","1","0","1","1","1","1","1","0"],
                             ["1","0","1","1","1","0","0","1","1","0","1","1","1","1","1","1","1","1","1","1"],
                             ["1","1","1","1","0","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1"],
                             ["1","0","0","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1"],
                             ["1","0","1","1","1","1","1","1","0","1","1","1","0","1","1","1","0","1","1","1"],
                             ["0","1","1","1","1","1","1","1","1","1","1","1","0","1","1","0","1","1","1","1"],
                             ["1","1","1","1","1","1","1","1","1","1","1","1","0","1","1","1","1","0","1","1"],
                             ["1","1","1","1","1","1","1","1","1","1","0","1","1","1","1","1","1","1","1","1"],
                             ["1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1"],
                             ["0","1","1","1","1","1","1","1","0","1","1","1","1","1","1","1","1","1","1","1"],
                             ["1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1"],
                             ["1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1"],
                             ["1","1","1","1","1","0","1","1","1","1","1","1","1","0","1","1","1","1","1","1"],
                             ["1","0","1","1","1","1","1","0","1","1","1","0","1","1","1","1","0","1","1","1"],
                             ["1","1","1","1","1","1","1","1","1","1","1","1","0","1","1","1","1","1","1","0"],
                             ["1","1","1","1","1","1","1","1","1","1","1","1","1","0","1","1","1","1","0","0"],
                             ["1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1"],
                             ["1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1"],
                             ["1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1"]]))