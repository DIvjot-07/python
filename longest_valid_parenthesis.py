class Solution(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        best=0
        stack=[-1]
        for i ,c in enumerate(s):
            if c =="(":
                stack.append(i)
            else:
                stack.pop()
                if not stack:
                    stack.append(i)
                else:
                    best=max(best,i-stack[-1])
        return best
