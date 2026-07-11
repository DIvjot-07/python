class Solution(object):
    def concatWithReverse(self, nums):
        n=len(nums)
        ans=[]
        for i in range(n):
            ans.append(nums[i])
        for i in range(n-1,-1,-1):
            ans.append(nums[i])
        return ans

print(Solution().concatWithReverse([1,2,3]))