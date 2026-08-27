class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        return self.binary(nums,target,0,len(nums)-1)
        
    
    def binary(self,nums,target,low,high):
            if(low>high):
                return high+1
            mid=(low+high)//2
            if(nums[mid]==target):
                return mid
            elif(nums[mid]<target):
                return self.binary(nums,target,mid+1,high)
            else:
                return self.binary(nums,target,low,mid-1)
print(Solution().searchInsert( [1,3,5,6], target = 7))