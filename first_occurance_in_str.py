class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if needle not in haystack:
            return -1
        i=0
        while(i<len(haystack)-len(needle)+1):
            if(needle == haystack[i:len(needle)+i]):
                return i
            else:
                i+=1
