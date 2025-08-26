class Solution(object):
    def longestConsecutive(self, nums):
        num_set = set(nums)
        longest_streak = 0

        for num in num_set:
            if num - 1 not in num_set:
                current_num = num
                current_streak = 1

                while current_num + 1 in num_set:
                    current_num += 1
                    current_streak += 1

                longest_streak = max(longest_streak, current_streak)

        return longest_streak
k=Solution()
print(k.longestConsecutive([100,4,200,1,3,2]))  # Output: 4   print(Solution(longestConsecutive([100,4,200,1,3,2])))  # Output: 4