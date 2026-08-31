from collections import Counter
class Solution(object):
    def checkInclusion(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        len1,len2=len(s1),len(s2)
        count=Counter(s1)
        window=Counter(s2[:len1])
        if count==window:
            return True
        for i in range(len1,len2):
            window[s2[i]]+=1
            left=s2[i-len1]
            window[s2[left]]-=1
            if(window[left] == 0):
                del window[left]
            if count==window:
                return True
        return False