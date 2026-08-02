from collections import Counter
class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        count=Counter(p)
        window=Counter(s[:len(p)])
        result=[]
        left,right=0,len(p)-1
        while(right<len(s)):#"cbaebabacd" left=0,right=2
            if(window==count):
                result.append(left)
            right+=1
            if(right<len(s)):
                window[s[left]]-=1
                if window[s[left]]==0:
                    del window[s[left]]
                left+=1
                window[s[right]]+=1
        return result