import re
class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        t=re.sub(r'[^a-zA-Z0-9]','',s)
        t=t.lower()
        if(t==t[::-1]):
            return True
        else:
            return False

print(Solution().isPalindrome("race a car"))