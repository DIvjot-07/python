class Solution(object):
    def numberOfSets(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """
        if k > n - 1:
            return 0
        p=1000000007
        fact=[1]*(n+k+1)
        invfact=[1]*(n+k+1)
        for i in range(2,n+k+1):
            fact[i]=(fact[i-1]*i)%p
        for i in range(2,n+k+1):
            invfact[i]=invfact[i-1] * pow(i, p-2, p) % p
        return (fact[n+k-1] * invfact[2*k] * invfact[n-k-1])%p
