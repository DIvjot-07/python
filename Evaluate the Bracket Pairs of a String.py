class Solution(object):
    def evaluate(self, s, knowledge):
        """
        :type s: str
        :type knowledge: List[List[str]]
        :rtype: str
        """
        stack=[]
        string=[]
        knowledge=dict(knowledge)
        for i in s:
            if i=="(":
                stack.append(i)
                
            elif i == ")":
                key="".join(stack[1::])
                string.append(knowledge.get(key,"?"))
                stack[:]=[]
                
            elif not stack :
                string.append(i)
            else: 
                stack.append(i)

        return "".join(string)
                
                
                
