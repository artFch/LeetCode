class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        set_nums = set(nums)  # множество не может содержать одинаковых чисел
        return len(set_nums) != len(nums)
