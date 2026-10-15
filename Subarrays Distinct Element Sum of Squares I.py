class Solution(object):
    def sumCounts(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count=0
        for i in range(len(nums)):
            for j in range(len(nums)):
                if i<j+1:
                    count+=(len(set(nums[i:j+1])))**2
        return count
