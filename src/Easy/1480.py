class Solution:
    def runningSum(self, nums: list[int]) -> list[int]:
        sum_nums = []
        k = 0
        for i in range(len(nums)):
            k += nums[i]
            sum_nums.append(k)
        return sum_nums
