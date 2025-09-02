class Solution(object):
    def shipWithinDays(self, weights, days):
        """
        :type weights: List[int]
        :type days: int
        :rtype: int
        """
        # Search space
        left, right = max(weights), sum(weights)

        def canShip(capacity):
            days_needed = 1
            current = 0
            for w in weights:
                if current + w > capacity:
                    days_needed += 1
                    current = 0
                current += w
            return days_needed <= days

        # Binary search
        while left < right:
            mid = (left + right) // 2
            if canShip(mid):
                right = mid
            else:
                left = mid + 1
        return left
