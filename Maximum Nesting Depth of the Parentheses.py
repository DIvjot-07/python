class Solution(object):
    def maxDepth(self, s):
        """
        :type s: str
        :rtype: int
        """
        res=0
        m=0
        for i in s:
            if i=="(":
                m+=1
            elif i == ")":
                res=max(res,m)
                m-=1
            else:
                pass
        return res
                
