from collections import Counter
class Solution(object):
    def firstUniqueFreq(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count=Counter(nums)
        freq=Counter(count.values())
        i=0
        while(i<len(nums)):
            if(freq[count[nums[i]]] == 1):
                return nums[i]
            else:
                i+=1
        return -1
