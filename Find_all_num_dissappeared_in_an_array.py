class Solution(object):
    def findDisappearedNumbers(self, nums):
        output=[]
        set_nums=set(nums)
        for i in range(1,len(nums)+1):
            if i in set_nums:
                pass
            else:
                output.append(i)
        return output
    
print(Solution().findDisappearedNumbers([1,1]))