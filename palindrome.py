class Solution(object):
    def isPalindrome(self, x):
        if(x < 0):
            return False
        y=0
        temp=x
        while(temp>0):
            y*=10
            y+=(temp%10)
            temp=temp//10

        if(y==x):
            return True
        else:
            return False

print(Solution().isPalindrome(1212))