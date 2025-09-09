def permuteUnique(nums):
    nums.sort()   # sort to handle duplicates
    res = []
    used = [False] * len(nums)

    def backtrack(path):
        if len(path) == len(nums):
            res.append(path[:])
            return
        
        prev = None
        for i in range(len(nums)):
            if used[i] or nums[i] == prev:  # skip used or duplicate at same level
                continue
            used[i] = True
            path.append(nums[i])
            backtrack(path)
            path.pop()
            used[i] = False
            prev = nums[i]

    backtrack([])
    return res


# Example usage
nums = list(map(int, input().split()))
print(permuteUnique(nums))


'''
from itertools import permutations
class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        return list(set(permutations(nums)))
        
'''
