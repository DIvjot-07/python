class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        result=[]
        w1,w2=0,0
        while(w1 != len(word1) and w2 != len(word2)):
            result.append(word1[w1])
            result.append(word2[w2])
            w1+=1
            w2+=1
        while(w1 != len(word1)):
            result.append(word1[w1])
            w1+=1
        while(w2 != len(word2)):
            result.append(word2[w2])
            w2+=1
        return "".join(result)

print(Solution().mergeAlternately(word1 = "abcd", word2 = "pq"))