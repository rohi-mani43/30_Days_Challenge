class Solution(object):
    def findTargetSumWays(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        memo = {}

        def dfs(index, curr_sum):
            # If reached end, check if target is met
            if index == len(nums):
                return 1 if curr_sum == target else 0
            
            # Memoization
            if (index, curr_sum) in memo:
                return memo[(index, curr_sum)]
            
            # Choose + or -
            add = dfs(index + 1, curr_sum + nums[index])
            subtract = dfs(index + 1, curr_sum - nums[index])
            
            memo[(index, curr_sum)] = add + subtract
            return memo[(index, curr_sum)]

        return dfs(0, 0)
