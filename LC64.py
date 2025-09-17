class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m, n = len(grid), len(grid[0])

        # DP table: overwrite grid to save space
        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0:
                    continue  # starting point
                elif i == 0:  # first row
                    grid[i][j] += grid[i][j-1]
                elif j == 0:  # first column
                    grid[i][j] += grid[i-1][j]
                else:  # min of top or left
                    grid[i][j] += min(grid[i-1][j], grid[i][j-1])

        return grid[m-1][n-1]
