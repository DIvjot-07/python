from collections import Counter
class Solution(object):
    def nextGreatestLetter(self, letters, target):
        """
        :type letters: List[str]
        :type target: str
        :rtype: str
        """
        count=Counter(letters)
        print(sorted(count.keys()))
        for i in sorted(count.keys()):
            if i > target:
                return i
        return letters[0]
print(Solution().nextGreatestLetter(letters = ["c","f","j","h"], target = "g"))