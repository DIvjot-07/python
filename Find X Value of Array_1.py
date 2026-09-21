class Solution(object):
    def resultArray(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        n = len(nums)
        result = [0] * k
        dp = [0] * k
        for i in range(n):
            ndp = [0] * k  
            ndp[nums[i] % k] += 1
            for r in range(k):
                ndp[(r * nums[i]) % k] += dp[r]
            dp = ndp
            for r in range(k):
                result[r] += dp[r]
        return result
