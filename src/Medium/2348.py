class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        sub = 0
        zeroes = 0
        for num in nums:
            if num == 0:
                zeroes += 1
                sub += zeroes
            else:
                zeroes = 0
        return sub
