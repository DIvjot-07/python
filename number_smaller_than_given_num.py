class Solution(object):
    def smallerNumbersThanCurrent(self, nums):
        output=[]
        left,right=0,len(nums)-1
        for i in range(len(nums)):
            count,left=0,0
            while(left <= right):
                if(nums[left] < nums[i]):
                    count+=1
                left+=1
            output.append(count)
        return output

print(Solution().smallerNumbersThanCurrent([7,7,7,7]))