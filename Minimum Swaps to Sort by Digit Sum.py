class Solution(object):
    def minSwaps(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        sums=[0]*len(nums)
        for i in range(len(nums)):
            for j in str(nums[i]):
                sums[i]+=int(j)
        cycles=0
        order = sorted(range(len(nums)), key=lambda i: (sums[i], nums[i]))
        target=[0]*len(nums)
        visited=[False]*len(nums)
        for k in range(len(nums)):
            target[order[k]]=k
        for i in range(len(nums)):
            if not visited[i]:
                j=i
                cycles+=1
                while not visited[j]:
                    visited[j]=True
                    j=target[j]
        return len(nums)-cycles
