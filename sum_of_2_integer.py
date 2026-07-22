class Solution(object):
    def getSum(self, a, b):
        mask = 0xFFFF
        max = 0x7FFF
        a &= mask
        b &= mask
        while(b!=0):
            sum_carry = (a & b) << 1
            a=(a ^ b) & mask
            b = sum_carry & mask

        return a if a <= max else ~(a ^ mask)
    
print(Solution().getSum(5,0))