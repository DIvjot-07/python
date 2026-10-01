class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if len(s)%2==1:
            return False
        stack=[]
        for i in s:
            if i in {"(","[","{"}:
                stack.append(i)
            elif stack and (i == ")" and stack[-1]=="(" or i == "]" and stack[-1]=="[" or i == "}" and stack[-1]=="{"):
                    stack.pop()
            else:
                return False
        return not stack
            
        
