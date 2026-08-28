class Solution(object):
    def search(self, nums, target):
        return self.binary(nums,target,0,len(nums)-1)
        
    def binary(self,nums,target,low,high):
        if(low>high):
            return -1
        mid=int((low+high)/2)
        if(nums[mid]==target):
                return mid
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
            
print(Solution().search([5,6,7,1,2,3,4],7))
        