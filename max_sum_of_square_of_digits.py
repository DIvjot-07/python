class Solution(object):
    def maxSumOfSquares(self, num, sum):
        """
        :type num: int
        :type sum: int
        :rtype: str
        """
        if sum > num*9:
            return ""
        q=sum//9
        r=sum%9
        ans="9"*q
        if r>0:
            ans+=str(r)
        ans+="0"*(num-len(ans))
        return ans
