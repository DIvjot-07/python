class Solution(object):
    def gcdOfOddEvenSums(self, n):
        """
        :type n: int
        :rtype: int
        """
        odd_sum,even_sum=0,0
        for i in range(n):#n=4 1,3,5,7
            odd_sum += i*2+1  
        for i in range(n):#n=4 2,4,6,8
            even_sum += i*2+2
        if(even_sum%odd_sum==0):
            return odd_sum
        else:
            i=odd_sum-1
            while(i!=1):
                if(even_sum%i==0 and odd_sum%i==0):
                    return i
                else:
                    i-=1
        return 1
