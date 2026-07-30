class Solution(object):
    def dailyTemperatures(self, temperatures):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """
        answer=[0]*len(temperatures)

        for i in range(len(temperatures)-2,-1,-1):
            j=i+1
            while(j<len(temperatures) and temperatures[j]<=temperatures[i]):
                if(answer[j] == 0):
                    j=len(temperatures)
                    break
                j+=answer[j]
            if j<len(temperatures):
                answer[i] = j - i
        return answer
