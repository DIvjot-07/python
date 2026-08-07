class Solution(object):
    DIGIT_FACTORS = {
        0: {}, 1: {}, 2: {2: 1}, 3: {3: 1}, 4: {2: 2},
        5: {5: 1}, 6: {2: 1, 3: 1}, 7: {7: 1}, 8: {2: 3}, 9: {3: 2}
    }

    def smallestNumber(self, num, t):
        primeCount, ok = self.get_prime_count(t)
        if not ok:
            return "-1"

        factorCount = self.get_factor_count(primeCount)
        if self.sum_values(factorCount) > len(num):
            return self.construct(factorCount)

        primeCountPrefix = self.get_prime_count_from_string(num)
        firstZeroIndex = num.find("0")
        if firstZeroIndex == -1:
            firstZeroIndex = len(num)
            if self.is_subset(primeCount, primeCountPrefix):
                return num

        n = len(num)
        for i in range(n - 1, -1, -1):
            d = int(num[i])
            primeCountPrefix = self.subtract(primeCountPrefix, self.DIGIT_FACTORS[d])
            spaceAfter = n - 1 - i

            if i > firstZeroIndex:
                continue

            for biggerDigit in range(d + 1, 10):
                remaining = self.subtract(self.subtract(primeCount, primeCountPrefix), self.DIGIT_FACTORS[biggerDigit])
                factorsAfterReplacement = self.get_factor_count(remaining)
                needed = self.sum_values(factorsAfterReplacement)
                if needed <= spaceAfter:
                    fillOnes = spaceAfter - needed
                    return num[:i] + str(biggerDigit) + "1" * fillOnes + self.construct(factorsAfterReplacement)

        factorsAfterExtension = self.get_factor_count(primeCount)
        return "1" * (n + 1 - self.sum_values(factorsAfterExtension)) + self.construct(factorsAfterExtension)

    def get_prime_count(self, t):
        count = {2: 0, 3: 0, 5: 0, 7: 0}
        for p in (2, 3, 5, 7):
            while t % p == 0:
                t //= p
                count[p] += 1
        return count, t == 1

    def get_prime_count_from_string(self, num):
        count = {2: 0, 3: 0, 5: 0, 7: 0}
        for c in num:
            for p, f in self.DIGIT_FACTORS[int(c)].items():
                count[p] += f
        return count

    def subtract(self, a, b):
        keys = set(a) | set(b)
        return {k: max(0, a.get(k, 0) - b.get(k, 0)) for k in keys}

    def sum_values(self, count):
        return sum(count.values())

    def is_subset(self, a, b):
        return all(b.get(k, 0) >= v for k, v in a.items())

    def get_factor_count(self, count):
        c2, c3, c5, c7 = count.get(2, 0), count.get(3, 0), count.get(5, 0), count.get(7, 0)
        count8 = c2 // 3
        remaining2 = c2 % 3
        count9 = c3 // 2
        count3 = c3 % 2
        count4 = remaining2 // 2
        count2 = remaining2 % 2
        count6 = 0

        if count2 == 1 and count3 == 1:
            count2, count3 = 0, 0
            count6 = 1

        if count3 == 1 and count4 == 1:
            count2 = 1
            count6 = 1
            count3, count4 = 0, 0

        return {2: count2, 3: count3, 4: count4, 5: c5, 6: count6, 7: c7, 8: count8, 9: count9}

    def construct(self, factors):
        parts = []
        for digit in range(2, 10):
            parts.append(str(digit) * factors.get(digit, 0))
        return "".join(parts)
