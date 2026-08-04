class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        first=self.binary(nums,target,0,len(nums)-1,True)
        if(first==-1):
            return [-1,-1]
        else:
            last=self.binary(nums,target,0,len(nums)-1,False)
            return[first,last]

    def binary(self,nums,target,low,high,isFirst):
        result=-1
        while low <= high:
            mid=int((low+high)/2)
            if(nums[mid]==target):
                result = mid
                if isFirst:
                    high = mid - 1   
                else:
                    low = mid + 1
            elif(nums[mid]<target):
                low=mid+1
            else:
                high=mid-1
        return result