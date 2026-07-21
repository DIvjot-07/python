class Solution(object):
    def findErrorNums(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n=len(nums)
        count=[0]*n
        for i in nums:
            count[i-1]+=1

        dup,mis=-1,-1
        for i in range(n):
            if(count[i]==2):
                dup=i+1
            elif(count[i]==0):
                mis=i+1
            else:
                pass
        return [dup,mis]
            
print(Solution().findErrorNums([1,2,2,4]))