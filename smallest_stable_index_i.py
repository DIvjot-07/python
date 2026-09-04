class Solution(object):
    def firstStableIndex(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        n=len(nums)
        left=[nums[0]]
        right=[-1]*n
        right[n-1]=nums[n-1]
        for i in range(1,n):
            left.append(max(left[i-1], nums[i]))
        for i in range(n-2,-1,-1):
            right[i]=min(right[i+1], nums[i])
        result=-1
        for i in range(0,n):
            if left[i] - right[i] <= k:
                result = i
                break
        return result
