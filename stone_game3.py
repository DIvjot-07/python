class Solution(object):
    def stoneGameIII(self, stoneValue):
        """
        :type stoneValue: List[int]
        :rtype: str
        """
        memo={}
        value=self.solve(0, stoneValue, memo)
        if(value>0):
            return "Alice"
        elif(value<0):
            return "Bob"
        return "Tie"
                    
    def solve(self,i, nums, memo):
        if i >= len(nums):
            return 0
        if i in memo:
            return memo[i]
        value = float('-inf')
        total = 0
        for k in range(3):
            if i + k >= len(nums):
                break
            total += nums[i + k]
            value = max(value, total - self.solve(i + k + 1, nums, memo))
        memo[i]=value
        return value