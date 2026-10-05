class Solution(object):
    def scoreOfParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        dp={}
        left = 0
        right = len(s)-1
        def score(i,j):
            if i>j:
                return 0
            if (i, j) in dp:
                return dp[i, j]
            if s[i:j+1]=="()":
                dp[i,j]=1
                return 1
            balance = 0
            for k in range(i, j + 1):
                balance += 1 if s[k] == '(' else -1
                if balance == 0:
                    break
            if k < j:
                dp[i, j] = score(i, k) + score(k + 1, j)
            else:
                dp[i,j]=2*score(i+1,j-1)
            return dp[i,j]
        score(left,right)
        return dp[left,right]
            
