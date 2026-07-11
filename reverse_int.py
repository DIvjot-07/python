class Solution(object):
    def reverse(self, x):
        if(x >= (-2**31) and x <= (2**31 - 1)):
            x=str(x)
            if(int(x)>=0):
                x=x[::-1]
                if(int(x) >= (-2**31) and int(x) <= (2**31 - 1)):
                    return int(x)
                else:
                    return 0
            else:
                x=x[:0:-1]
                if(int(x) >= (-2**31) and int(x) <= (2**31 - 1)):
                    return -int(x)
                else:
                    return 0
        else:
            return 0

print(Solution().reverse(1534236469))