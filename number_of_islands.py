class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        rows, cols = len(grid), len(grid[0])
        def Island(image, sr, sc):
            original = image[sr][sc]
            queue = deque([(sr, sc)])
            image[sr][sc] = '0'
            directions = [(-1,0), (1,0), (0,-1), (0,1)]
        
            while queue:
                r, c = queue.popleft()
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < rows and 0 <= nc < cols and image[nr][nc] == '1':
                        image[nr][nc] = '0'
                        queue.append((nr, nc))
            return
        count =0
        for i in range(rows):
            for j in range(cols):
                if grid[i][j]=='1':
                    Island(grid, i,j)
                    count +=1
        return count
                    
                    
            
