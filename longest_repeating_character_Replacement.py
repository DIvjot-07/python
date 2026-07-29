from collections import Counter
class Solution(object):
    def characterReplacement(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        freq=Counter(s[:0])
        left,right,length,window,max_freq=0,0,0,0,0
        while(right<len(s)):
            freq[s[right]]+=1
            right+=1
            window=right-left
            max_freq=max(freq.values())
            if(window-max_freq > k):
                freq[s[left]]-=1
                left+=1
                continue
            if(length<window):
                length=window
        return length