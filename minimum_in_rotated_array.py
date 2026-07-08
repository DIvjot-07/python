class Solution(object):
    def search(self, nums):
        min=nums[0]
        return self.binary(nums,min,0,len(nums)-1)
        
    def binary(self,nums,min,low,high):
        if(low<=high):
            mid=int((low+high)/2)
            if(nums[mid]<min):
                min=nums[mid]
            if nums[mid] > nums[high]:
                min=self.binary(nums,min,mid+1,high)
            if nums[mid] <= nums[high]:
                min=self.binary(nums,min,low,mid-1)

        return min
        
print(Solution().search([4,5,6,-2,-1,0,1,2,3]))