class Solution(object):
    def threeSumClosest(self, nums,target):
        nums.sort()
        n=len(nums)
        best=float('inf')

        for i in range(n-2):

            left,right=i+1,n-1
            while(left < right):
                total=nums[i]+nums[left]+nums[right]
                if abs(total - target) < abs(best - target):
                    best = total

                if total == target:
                    return total
                elif(total>target):
                    right-=1
                else:
                    left+=1
        return best
    

print(Solution().threeSumClosest([-1,2,1,-4], target = 1))