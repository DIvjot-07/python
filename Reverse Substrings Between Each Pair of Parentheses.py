class Solution(object):
    def reverseParentheses(self, s):
        """
        :type s: str
        :rtype: str
        """
        stack=[]
        string=[]
        i=0
        while i<len(s):
            if s[i] == "(":
                stack.append(s[i])
                i+=1
            elif s[i] == ")":
                while stack[-1]!= "(":
                    string.append(stack.pop())
                stack.pop()
                stack.extend(string)
                string[:]=[]
                i+=1
            else:
                stack.append(s[i])
                i+=1
        return "".join(stack)
                
