class Solution:
    def reverseDegree(self, s: str) -> int:
        m={}
        last=122
        sum=0
        for i in range(1,27):
            m[last]=i
            last-=1
        for i in range(1,len(s)+1):
            sum += (i*m[ord(s[i-1])])
        return sum
