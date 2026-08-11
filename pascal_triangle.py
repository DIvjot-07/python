class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        list=[[1]]
        for i in range(2,numRows+1):#i=3 [1,1,1]
            List=[1]*i
            for j in range(1,i-1):#[1,1,1] j=1 list[1]=[1,1]
                List[j]=list[i-2][j-1]+list[i-2][j] #List[1]=1+1 [1,2,1]
            list.append(List)
        return list
                