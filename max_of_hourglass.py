class Solution(object):
    def maxSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m=len(grid)
        n=len(grid[0])
        max=-float('inf')
        for i in range(m-2):
            for j in range(n-2):
                sum=grid[i][j] + grid[i][j+1] + grid[i][j+2] + grid[i+1][j+1] + grid[i+2][j] + grid[i+2][j+1] + grid[i+2][j+2]
                if(sum>max):
                    max=sum
        return max
    
print(Solution().maxSum([[6,2,1,3],[4,2,1,5],[9,2,8,7],[4,1,2,9]]))