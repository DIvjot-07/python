class Solution(object):
    def validSequence(self, word1, word2):
        n = len(word1)
        m = len(word2)

        suffix = [0] * (n + 1)
        j = m - 1
        for i in range(n - 1, -1, -1):
            if j >= 0 and word1[i] == word2[j]:
                j -= 1

            suffix[i] = m - 1 - j

        result = []
        j = 0
        used_change = False

        for i in range(n):
            if j == m:
                break
            if word1[i] == word2[j]:
                result.append(i)
                j += 1
            elif not used_change and suffix[i + 1] >= m - j - 1:
                result.append(i)
                j += 1
                used_change = True

        if j < m:
            return []
        return result
