class Solution(object):
    def maxArea(self, height):
        profit=0
        left,right=0,len(height)-1
        while(left < right):
            A=self.Area(height,left,right)
            profit = max(A, profit)
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
                
        return profit

    def Area(self,height,i1,i2):
        x=abs(i1-i2)
        y=(min(height[i1],height[i2]))
        return x*y

print(Solution().maxArea([1,8,6,2,5,4,8,3,7]))