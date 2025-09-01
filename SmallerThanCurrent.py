class Solution(object):
    def smallerNumbersThanCurrent(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        sorted_nums = sorted(nums)
        
        count_map = {}
        for i, num in enumerate(sorted_nums):
            if num not in count_map:
                count_map[num] = i
        return [count_map[num] for num in nums]
