class Solution(object):
    def minInsertions(self, s):
        """
        :type s: str
        :rtype: int
        """
        count=0
        stack=[]
        missing=0
        for i in s:
            if i == '(':
                end=0
                if count==1:
                    missing += 1
                    if stack:
                        stack.pop()
                    else:
                        missing += 1      
                    count = 0
                stack.append(i)
            else:
                count += 1
                if count == 2:
                    if stack:
                        stack.pop()
                    else:
                        missing += 1    
                    count = 0

        if count == 1:
            missing += 1                  
            if stack:
                stack.pop()
            else:
                missing += 1
                    
        return missing + len(stack)*2
                
        
