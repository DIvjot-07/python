class Solution(object):
    def stoneGame(self, piles):
        """
        :type piles: List[int]
        :rtype: bool
        """
        memo={}
        value=self.solve(0, len(piles)-1, piles, memo)
        if(value>0):
            return True
        return False
                    
    def solve(self,i, j, nums, memo):
        if (i, j) in memo:
            return memo[i, j]
        if(i==j):
            memo[i,j]=nums[i]
            return nums[i]
        value=max(nums[i] - self.solve(i+1,j,nums, memo), nums[j] - self.solve(i,j-1,nums, memo))
        memo[i,j]=value
        return value