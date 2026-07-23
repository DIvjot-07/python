class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        result=s.split(" ")
        i=-1
        while(i>=-len(result)):
            if(len(result[i])>0):
                return len(result[i])
            else:
                i-=1
s="a"
print(Solution().lengthOfLastWord(s))
