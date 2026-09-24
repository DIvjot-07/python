class Solution(object):
    def smallestIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        def smallest(n,i):
            sum=0
            if n==1000:
                sum=1
            else:
                if n<10:
                    sum+=n
                elif n>=10 and n<100:
                    sum+=n//10
                    n=n%10
                    sum+=n
                else:
                    sum+=n//100
                    n=n%100
                    sum+=n//10
                    n=n%10
                    sum+=n
            if sum==i:
                return i
            return -1
        for i in range(len(nums)):
            m=-1
            m=smallest(nums[i],i)
            if m != -1:
                return m
        return -1
