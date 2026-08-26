class Solution(object):
    def searchMatrix(self, matrix, target):
        m=len(matrix)
        n=len(matrix[0])
        row,col=0,n-1
        while(row < m and col >= 0):
            val=matrix[row][col]
            if val == target:
                return True
            elif(val > target):
                col-=1
            elif(val < target):
                row+=1
            else:
                return False
                
        return False

print(Solution().searchMatrix([[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]], target = 20))