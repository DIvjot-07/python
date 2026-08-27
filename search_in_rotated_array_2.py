class Solution(object):
    def search(self, nums, target):
        return self.binary(nums,target,0,len(nums)-1)
        
    def binary(self,nums,target,low,high):
        if(low>high):
            return False
        mid=int((low+high)/2)
        if(nums[mid]==target):
                return True
        if nums[low] == nums[mid] == nums[high]:
            return self.binary(nums, target, low + 1, high - 1)
        if nums[low] <= nums[mid]:
            if nums[low] <=target < nums[mid]:
                return self.binary(nums,target,low,mid-1)
            else:
                return self.binary(nums,target,mid+1,high)
        else:
            if nums[mid] < target <= nums[high]:
                return self.binary(nums,target,mid+1,high)
            else:
                return self.binary(nums,target,low,mid-1)
            
print(Solution().search([1,0,1,1,1],0))