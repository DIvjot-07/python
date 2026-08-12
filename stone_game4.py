class Solution(object):
    def winnerSquareGame(self, n):
        """
        :type n: int
        :rtype: bool
        """
        win=[False]*(n+1)
        for i in range(1,n+1):
            j=1
            while(j*j <= i):
                if win[i - j*j] == False:
                    win[i]=True
                    break
                j+=1

        return win[n]
