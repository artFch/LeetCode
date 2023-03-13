class Solution:
    def findKthPositive(self, arr: list[int], k: int) -> int:
        n = 0
        for i in range(1, max(arr)):
            if i not in arr:
                n += 1
            if n == k:
                return i
        return max(arr) + k - n
