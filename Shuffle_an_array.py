import random
class Solution(object):

    def __init__(self, nums):
        self.original  = list(nums)
        self.nums=nums
        

    def reset(self):
        self.nums = list(self.original)
        return self.nums

    def shuffle(self):
        for i in range(len(self.nums)):
            j=random.randint(0,i)
            self.nums[i],self.nums[j]=self.nums[j],self.nums[i]
        return self.nums
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()
obj=Solution([1,2,3,4])
print(obj.nums)
print(obj.shuffle())
print(obj.reset())
print(obj.shuffle())
print(obj.reset())