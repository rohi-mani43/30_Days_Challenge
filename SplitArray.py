class Solution(object):
    def splitArray(self, nums, k):
        def canSplit(maxSum):
            subarrays = 1
            currentSum = 0
            
            for num in nums:
                if currentSum + num > maxSum:
                    subarrays += 1
                    currentSum = num
                else:
                    currentSum += num
            
            return subarrays <= k
        
        left = max(nums)
        right = sum(nums)
        
        while left < right:
            mid = (left + right) // 2
            if canSplit(mid):
                right = mid
            else:
                left = mid + 1
        
        return left
