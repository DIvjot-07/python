class Solution(object):
    def maxPalindromes(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        i=0
        count=0
        def is_palindrome(s):
            if s == s[::-1]:
                return True
            return False
        n = len(s)
        while i < n:
            taken = False
            for length in (k, k + 1):
                if i + length <= n and is_palindrome(s[i:i+length]):
                    count += 1
                    i += length
                    taken = True
                    break
            if not taken:
                i += 1
        return count
    
