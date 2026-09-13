class Solution(object):
    def largestOverlap(self, img1, img2):
        """
        :type img1: List[List[int]]
        :type img2: List[List[int]]
        :rtype: int
        """
        count1=[]
        count2=[]
        for i in range(0,len(img1[0])):
            for j in range(0,len(img1[0])):
                if img1[i][j]==1:
                    count1.append((i,j))
                if img2[i][j]==1:
                    count2.append((i,j))
                    
        shift={}
        for i in count1:
            for j in count2:
                dx, dy = i[0]-j[0],i[1]-j[1]
                shift[(dx,dy)] = shift.get((dx,dy), 0) + 1
            
        if shift:
            return max(shift.values())
        else:
            return 0
        

            
