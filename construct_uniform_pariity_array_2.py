class Solution(object):
    def uniformArray(self, nums1):
        """
        :type nums1: List[int]
        :rtype: bool
        """
        odd, even=0,0
        m=float("inf")
        n=float("inf")
        for i in nums1:
            if n>i:
                n=i
            if i%2 == 0:
                even += 1
            else:
                if i<m:
                    m=i
                odd += 1
            
        if odd == 0 or m == n:
            return True 
        return False
