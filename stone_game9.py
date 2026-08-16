class Solution(object):
    def stoneGameIX(self, stones):
        """
        :type stones: List[int]
        :rtype: bool
        """
        count =[0,0,0]
        for n in stones:
            count[n%3] += 1
        
        if count[0] % 2 == 0:
            return count[1] > 0 and count[2] > 0
        else:
            return abs(count[1] - count[2]) > 2