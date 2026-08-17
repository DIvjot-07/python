class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x==0:
            return 0
        guess=x/2.0
        tol=1e-10
        while True:
            better=0.5*(guess+x/guess)
            if(abs(guess-better)<tol):
                return int(better)
            guess=better