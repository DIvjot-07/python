class Solution(object):
    def maxNumberOfFamilies(self, n, reservedSeats):
        """
        :type n: int
        :type reservedSeats: List[List[int]]
        :rtype: int
        """
        reserved=set(map(tuple,reservedSeats))
        rows_with_reservations = set(r for r,c in reservedSeats if 1<=r<=n)
        count=0
        for i in rows_with_reservations:
            if (i,2) not in reserved and (i,3) not in reserved and (i,4) not in reserved and (i,5) not in reserved and (i,6) not in reserved and (i,7) not in reserved and (i,8) not in reserved and (i,9) not in reserved:
                count+=2
            elif (i,2) not in reserved and (i,3) not in reserved and (i,4) not in reserved and (i,5) not in reserved:
                count+=1 
            elif (i,6) not in reserved and (i,7) not in reserved and (i,8) not in reserved and (i,9) not in reserved:
                count+=1 
            elif (i,4) not in reserved and (i,5) not in reserved and (i,6) not in reserved and (i,7) not in reserved:
                count+=1 
            else:
                continue
        count += (n - len(rows_with_reservations)) * 2 
        return count


print(Solution().maxNumberOfFamilies(n = 3, reservedSeats = [[1,2],[1,3],[1,8],[2,6],[3,1],[3,10]]))
