class Solution(object):
    def isBalanced(self, num):
        """
        :type num: str
        :rtype: bool
        """
        num1,num2=0,0
        for i in range(len(num)):
            if(i%2==0):
                num1+=int(num[i])
            else:
                num2+=int(num[i])
        if(num1==num2):
            return True
        else:
            return False
print(Solution().isBalanced("24123"))