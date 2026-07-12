class Solution(object):
    def divide(self, dividend, divisor):
        mini=-2**31
        maxi=2**31 - 1
        ans=0
        if(dividend == mini and divisor == -1):
            return maxi
        
        divi=dividend
        div=divisor
        
        if(dividend<0):
            dividend_sign=-1
            dividend=abs(dividend)
        else:
            dividend_sign=1

        if(divisor<0):
            divisor_sign=-1
            divisor=abs(divisor)
        else:
            divisor_sign=1
        
        if(div <= maxi and divi <= maxi and div >= mini and divi >= mini and divisor!=0):
            while(dividend>=divisor):
                count=divisor
                multiple=1
                while(count <= dividend):
                    count = count << 1
                    multiple = multiple << 1
                ans+=multiple >>1
                dividend-=count>>1
        if((divisor_sign==1 and dividend_sign==1) or (divisor_sign==-1 and dividend_sign==-1)):
            return ans
        else:
            return -ans
        
print(Solution().divide(-2**31,-3))