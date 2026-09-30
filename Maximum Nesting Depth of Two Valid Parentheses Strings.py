class Solution(object):
    def maxDepthAfterSplit(self, seq):
        """
        :type seq: str
        :rtype: List[int]
        """
        answer=[0]*len(seq)
        count=0
        for i in range(0,len(seq)):
            if seq[i] == "(":
                count+=1
                answer[i]=count%2
            else:
                answer[i]=count%2
                count-=1
        return answer 
