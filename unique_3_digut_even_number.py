from collections import Counter

class Solution(object):
    def totalNumbers(self, digits):
        """
        :type digits: List[int]
        :rtype: int
        """
        count = 0
        Count = Counter(digits)  # <-- must count the input digits
        for i in range(100, 1000, 2):
            hundred = i // 100
            ten = i // 10 - hundred * 10
            one = i - hundred * 100 - ten * 10
            need = Counter([hundred, ten, one])
            if all(Count[d] >= c for d, c in need.items()):
                count += 1
        return count
