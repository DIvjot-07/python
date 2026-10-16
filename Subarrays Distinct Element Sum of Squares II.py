class Solution(object):
    def sumCounts(self, nums):
        MOD = 10**9 + 7
        n = len(nums)
        b1 = [0] * (n + 2)
        b2 = [0] * (n + 2)

        def upd(b, i, v):
            while i <= n + 1:
                b[i] += v
                i += i & -i

        def qry(b, i):
            s = 0
            while i > 0:
                s += b[i]
                i -= i & -i
            return s

        def prefix(i):
            return qry(b1, i) * i - qry(b2, i)

        last = {}
        cur = ans = 0
        for r, x in enumerate(nums):
            a = last.get(x, -1)+2
            b = r + 1       
            length = b - a + 1
            rs = prefix(b) - prefix(a - 1)  
            cur += 2 * rs + length
            upd(b1, a, 1);  upd(b1, b + 1, -1)
            upd(b2, a, a - 1);  upd(b2, b + 1, -b)
            ans += cur
            last[x] = r
        return ans % MOD
