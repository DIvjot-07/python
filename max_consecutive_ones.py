class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        counts=0
        i=0
        while i < len(nums):
            if nums[i]==1 :
                count=0
                while(i<len(nums) and nums[i]==1):
                    count+=1
                    i+=1
                    if(counts<count):
                        counts=count
            else:
                i+=1
        return counts
    
print(Solution().findMaxConsecutiveOnes([1,1,0,1,1,1,0]))