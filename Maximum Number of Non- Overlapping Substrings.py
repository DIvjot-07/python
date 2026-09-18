class Solution(object):
    def maxNumOfSubstrings(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        first = {}
        last = {}
        for i, ch in enumerate(s):
            if ch not in first:
                first[ch] = i
            last[ch] = i

        n = len(s)
        intervals = []
        for i in range(n):
            if i != first[s[i]]:
                continue 
            start = i
            end = last[s[i]]
            j = start
            valid = True
            while j <= end:
                ch = s[j]
                if first[ch] < start:
                    valid = False
                end = max(end, last[ch])
                j += 1

            if valid:
                intervals.append((start, end))
        intervals.sort(key=lambda x: (x[1], x[0]))
        result = []
        prev_end = -1
        for start, end in intervals:
            if start > prev_end:
                result.append(s[start:end+1])
                prev_end = end

        return result
