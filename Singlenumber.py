class Solution(object):
    def singleNumber(self, nums):
        
        k=set(nums)
        for i in k:
            if nums.count(i)==1:
                return i
        