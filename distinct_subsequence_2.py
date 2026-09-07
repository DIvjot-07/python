class Solution:
    def distinctSubseqII(self, s):
        MOD = 10**9 + 7
        dp = 1  # dp includes empty subsequence (base case)
        last = [0] * 26
        for c in s:
            idx = ord(c) - ord('a')
            new_dp = (2 * dp - last[idx]) % MOD
            last[idx] = dp      # store OLD dp before update
            dp = new_dp
        return (dp - 1) % MOD   # subtract the empty subsequence
