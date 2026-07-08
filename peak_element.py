class Solution(object):
    def findPeakElement(self, nums):
        return self.binary(nums,0,len(nums)-1)


    def binary(self,nums,low,high):
        if(low==high):
            return low
        mid=int((high+low)/2)
        if(nums[mid]<nums[mid+1]):
            return self.binary(nums,mid+1,high)
        if(nums[mid] > nums[mid+1]):
            return self.binary(nums,low,mid)
    
print(Solution().findPeakElement([1,2,1,3,5,6,4]))