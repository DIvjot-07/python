class Solution(object):
    def resultArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        arr1 = [nums[0]]
        arr2 = [nums[1]]

        for i in range(2, len(nums)):
            if arr1[-1] >= arr2[-1]:
                arr1.append(nums[i])
            else:
                arr2.append(nums[i])

        for i in arr2:
            arr1.append(i)

        return arr1
