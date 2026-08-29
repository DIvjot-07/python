class Solution(object):
    def lexicographicallySmallestArray(self, nums, limit):
        """
        :type nums: List[int]
        :type limit: int
        :rtype: List[int]
        """
        
        pairs = sorted(enumerate(nums), key=lambda x: x[1])
        groups = []
        current_group = [pairs[0]]

        for i in range(1, len(pairs)):
            prev_val = pairs[i-1][1]
            curr_val = pairs[i][1]
            if curr_val - prev_val <= limit:
                current_group.append(pairs[i])
            else:
                groups.append(current_group)
                current_group = [pairs[i]]

        groups.append(current_group) 

        result = [0] * len(nums)

        for group in groups:
            indices = sorted(idx for idx, val in group)
            values = sorted(val for idx, val in group)
            for idx, val in zip(indices, values):
                result[idx] = val


        return result