class Solution(object):
    def checkValidString(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if s[-1]=="(" or s[0]==")":
            return False
        stack=[]
        star=[]
        for i,c in enumerate(s):
            if c == "*":
                star.append(i)
            elif c == "(":
                stack.append(i)
            else:
                if stack:
                    stack.pop()
                elif star:
                    star.pop()
                else:
                    return False
        while stack and star :
            if stack.pop()>star.pop():
                return False
        return not stack
        
                    
