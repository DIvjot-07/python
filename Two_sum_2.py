class Solution(object):

    def twoSum2(self, nums, target):
        left,right=0,len(nums)-1
        while(left<right):
            s = nums[left] + nums[right]
            if(s==target):
                return [left+1,right+1]
            if(s>target):
                right-=1
            else:
                left+=1

print(Solution().twoSum2([5,25,75], target = 100))