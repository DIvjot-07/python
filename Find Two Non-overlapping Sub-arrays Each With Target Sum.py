class Solution(object):
    def minSumOfLengths(self, arr, target):
        n = len(arr)
        best = [float('inf')] * n
        ans = float('inf')

        total = 0
        left = 0

        for right in range(n):
            total += arr[right]

            while total > target:
                total -= arr[left]
                left += 1

            if total == target:
                window = right - left + 1
                if left > 0 and best[left-1] != float('inf'):
                    ans = min(ans, best[left-1] + window)
                best[right] = min(best[right-1] if right > 0 else float('inf'), window)
            else:
                best[right] = best[right-1] if right > 0 else float('inf')

        return ans if ans != float('inf') else -1
