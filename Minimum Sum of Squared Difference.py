class Solution(object):
    def minSumSquareDiff(self, nums1, nums2, k1, k2):
        k = k1 + k2
        diff = sorted((abs(a - b) for a, b in zip(nums1, nums2)), reverse=True)
        if sum(diff) <= k:
            return 0
        diff.append(0)  # sentinel

        i = 0  # top i+1 values are all leveled to diff[i]
        while i < len(diff) - 1:
            cost = (i + 1) * (diff[i] - diff[i + 1])
            if k >= cost:
                k -= cost
                i += 1
            else:
                break

        cnt = i + 1
        level = diff[i]
        drop, rem = divmod(k, cnt)
        level -= drop
    
        total = rem * (level - 1) ** 2 + (cnt - rem) * level ** 2
        total += sum(d * d for d in diff[cnt:])
        return total
