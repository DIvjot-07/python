class Solution(object):
    def findMissingElements(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        if not nums:
            return []
        s=set(nums)
        mini=min(nums)
        maxi=max(nums)
        result=[]
        for i in range(mini,maxi+1):
            if i not in s:
                result.append(i)
        return result