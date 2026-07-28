class Solution(object):
    def validPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s=list(s)
        left,right,k=0,len(s)-1,0
        while(left<right):
            if(s[left]==s[right]):
                left+=1
                right-=1
            else:
                return self.is_palindrome(s,left+1, right) or self.is_palindrome(s,left, right-1)
        return True
    def is_palindrome(self,s,left, right):
            while left < right:
                if s[left] != s[right]:
                    return False
                left += 1
                right -= 1
            return True