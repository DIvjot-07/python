class Solution(object):
    def smallestNumber(self, n, t):
        """
        :type n: int
        :type t: int
        :rtype: int
        """
        return self.prod(n, t)

    def prod(self, n, t):
        product = 1
        num = str(n)
        for i in num:
            product *= int(i)
        if product % t == 0:
            return n
        else:
            n += 1
            return self.prod(n, t)
