class Solution(object):
    def search(self, nums, target):
        return self.binary(nums,target,0,len(nums)-1)
        
    def binary(self,nums,target,low,high):
        if(low>high):
            return -1
        mid=int((low+high)/2)
        if(nums[mid]==target):
            return mid
        elif(nums[mid]<target):
            return self.binary(nums,target,mid+1,high)
        else:
            return self.binary(nums,target,low,mid-1)
        
        
            
print(Solution().search([-1,0,3,5,9,12], target = 9))