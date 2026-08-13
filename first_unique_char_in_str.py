from collections import Counter
class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        count=Counter(s)
        i=0
        while(i<len(s)):
            if count[s[i]] == 1:
                return i
            else:
                i+=1
        return -1