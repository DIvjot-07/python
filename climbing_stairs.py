class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        Fib=[0]*(n+2)
        Fib[1]=1
        for i in range(2,n+2):
            Fib[i]=Fib[i-2]+Fib[i-1]
        return Fib[n+1]