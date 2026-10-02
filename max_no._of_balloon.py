class Solution(object):
    def maxNumberOfBalloons(self, text):
        """
        :type text: str
        :rtype: int
        """
        count1={}
        count=Counter(text)
        for i in "balon":
            count1[i]=count[i]
        count1['o']=count1['o']//2
        count1['l']=count1['l']//2
        return min(count1.values()
