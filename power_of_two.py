class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n <= 0:
            return False
        return self.power_or_not(n)

    def power_or_not(self,n):
        if n == 1:
            return True
        elif n % 2 == 0:
            return self.power_or_not(n//2)
        else:
            return False