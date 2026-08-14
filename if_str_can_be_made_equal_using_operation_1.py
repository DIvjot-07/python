class Solution(object):
    def canBeEqual(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        if(s1==s2):
            return True
        elif(s1[0]==s2[0] and s1[2]==s2[2] and s1[1]==s2[3] and s1[3]==s2[1]):
            return True
        elif(s1[0]==s2[2] and s1[2]==s2[0] and s1[1]==s2[3] and s1[3]==s2[1]):
            return True
        elif(s1[0]==s2[2] and s1[2]==s2[0] and s1[3]==s2[3] and s1[1]==s2[1]):
            return True
        else:
            return False