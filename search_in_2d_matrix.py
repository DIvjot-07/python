class Solution(object):
    def searchMatrix(self, matrix, target):
        m=len(matrix)
        n=len(matrix[0])
        if m==1:
            count=1
        else:
            count=0
            
        left,right=0,m-1
        while(left<=right):
            if(matrix[left][n-1] >= target and target >= matrix[left][0]):
                return self.binary(matrix[left],target,0,n-1)
            elif(matrix[right][n-1] >= target and target >= matrix[right][0]):
                return self.binary(matrix[right],target,0,n-1)
            elif(count==0 and matrix[right-1][n-1] >= target and target >= matrix[left+1][0]):
                left+=1
                right-=1
            else:
                return False

    def binary(self,nums,target,low,high):
        if(low>high):
            return False
        mid=int((low+high)/2)
        if(nums[mid]==target):
            return True
        elif(nums[mid]<target):
            return self.binary(nums,target,mid+1,high)
        else:
            return self.binary(nums,target,low,mid-1)

m=[[1,2],[3,4],[5,6]]
print(Solution().searchMatrix(m,7))