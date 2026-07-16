class Solution(object):
    def thirdMax(self, nums):
        
        max1, max2, max3 = float('-inf'), float('-inf'), float('-inf')
        L=len(nums)

        for i in range(L):
            if(max1 < nums[i]):
                max3=max2
                max2=max1
                max1=nums[i]
            
            elif(max2 < nums[i] and nums[i] != max1):
                max3=max2
                max2=nums[i]
            
            elif(max3 < nums[i] and nums[i] != max2 and nums[i]!=max1):
                max3=nums[i]

        if(L<3 or max3==float('-inf')):
            return max1
        else :
            return max3



print(Solution().thirdMax([1,2,3]))