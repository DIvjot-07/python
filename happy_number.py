class Solution(object):
    def isHappy(self, n):
        seen=set()
        while(n!=1 and n not in seen):
            seen.add(n)
            num=0
            while(n!=0):
                num+=(n%10)**2
                n=n//10
            n=num
        if(n==1):
            return True
        else:
            return False

print(Solution().isHappy(19))
