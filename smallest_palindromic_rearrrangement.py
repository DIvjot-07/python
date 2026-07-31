from collections import Counter
class Solution(object):
    def smallestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        count=Counter(s)
        first=[]
        mid=""
        for i in sorted(count.keys()):
            c=count[i]
            if(c % 2 != 0):
                mid=i
            first.append(i * (c//2))
        return "".join(first) + mid + "".join(first[::-1])
                         