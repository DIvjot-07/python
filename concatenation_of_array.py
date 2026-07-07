class Solution(object):
    def getConcatenation(self, nums):
        ans=[]
        i=0
        while(i < 2*len(nums)):
            ans.append(nums[i % len(nums)])
            i+=1
        return ans
    
print(Solution().getConcatenation([1,2,3,2]))