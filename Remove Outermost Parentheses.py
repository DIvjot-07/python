class Solution(object):
    def removeOuterParentheses(self, s):
        """
        :type s: str
        :rtype: str
        """
        stack=[]
        string=[]
        out = False
        for i in s:
            if i == "(":
                if out:
                    string.append(i)
                else:
                    out=True
                stack.append(i)
            else:
                if out and len(stack)>1:
                    stack.pop()
                    string.append(i)
                else:
                    out = False
                    stack.pop()
        return "".join(string)
                
                
