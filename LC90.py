class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
   
        nums.sort()
        res = [[]]
        prev_end = 0
        for i in range(len(nums)):
            start = 0
            if i > 0 and nums[i] == nums[i-1]:
                start = prev_end
            prev_end = len(res)
            for j in range(start, len(res)):
                res.append(res[j] + [nums[i]])
        return res
                            