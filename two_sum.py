class Solution(object):

    def twoSum(self, nums, target):
        L=len(nums)
        result=[]
        for i in range(L):
            for j in range(i+1,L):
                if(nums[i] + nums[j] == target):
                    result.append(i)
                    result.append(i+1)
        return result

My=Solution()
print(My.twoSum([3,3],6))