class Solution(object):
    def hasValidPath(self, grid):
        m, n = len(grid), len(grid[0])
        if (m + n - 1) % 2 or grid[0][0] == ")" or grid[-1][-1] == "(":
            return False

        seen = set()

        def dfs(i, j, bal):
            bal += 1 if grid[i][j] == "(" else -1
            if bal < 0 or bal > (m - i) + (n - j):  
                return False
            if i == m - 1 and j == n - 1:
                return bal == 0
            if (i, j, bal) in seen:
                return False
            seen.add((i, j, bal))
            return (i + 1 < m and dfs(i + 1, j, bal)) or \
                   (j + 1 < n and dfs(i, j + 1, bal))

        return dfs(0, 0, 0)
