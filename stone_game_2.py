class Solution(object):
    def stoneGameII(self, piles):
        """
        :type piles: List[int]
        :rtype: int
        """
        self.dp={}
        m=1
        left=0
        self.n=len(piles)
        self.suffixSum=[0]*(self.n+1)
        for i in range(self.n-1,-1,-1):
            self.suffixSum[i]=self.suffixSum[i+1]+piles[i]
        return self.pilepicker(piles, 0, 1)

    def pilepicker(self,piles,left,m):
        if (left, m) in self.dp: 
            return self.dp[(left, m)]
        if(self.n - left <= 2*m):
            return self.suffixSum[left]

        best=-float('inf')
        for X in range(1,min(2*m , self.n - left)+1):
            result=self.suffixSum[left] - self.pilepicker(piles, left + X, max(m, X))
            best = max(best, result)
        self.dp[(left, m)] = best
        return best

