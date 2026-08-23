from collections import Counter

class Solution(object):
    def sumGame(self, num):
        """
        :type num: str
        :rtype: bool
        """
        mid = len(num) // 2
        first, second = 0, 0
        cnt1, cnt2 = 0, 0

        for i in range(0, mid):
            if num[i] != "?":
                first += int(num[i])
            else:
                cnt1 += 1

        for i in range(mid, len(num)):
            if num[i] != "?":
                second += int(num[i])
            else:
                cnt2 += 1

        if (cnt1 + cnt2) % 2 == 1:
            return True

        diff = first - second
        final_diff = diff + 9 * (cnt1 - cnt2) // 2
        return final_diff != 0
                





        

    
print(Solution().sumGame("2343?"))