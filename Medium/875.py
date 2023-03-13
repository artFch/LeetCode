import math


class Solution:
    def minEatingSpeed(self, piles, H):
        def condition(speed) -> bool:
            # condition
            return sum(math.ceil(pile / speed) for pile in piles) <= H

        left, right = 1, max(piles)
        while left < right:
            mid = left + (right - left) // 2
            if condition(mid):
                right = mid
            else:
                left = mid + 1
        return left
