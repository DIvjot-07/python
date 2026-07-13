class Solution(object):
    def containsDuplicate(self, nums):
        nums=sorted(nums)
        left,right=0,len(nums)-1
        while(left<right):
            if(nums[left]==nums[left+1]):
                return True
            else:
                left+=1

        return False

print(Solution().containsDuplicate([1,2,3,4]))