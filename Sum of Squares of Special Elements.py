class Solution(object):
    def sumOfSquares(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        total=0
        n=len(nums)
        for i in range(1,n+1):
            if n%(i)==0:
                total+=nums[i-1]**2
        return total 
