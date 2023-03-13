class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        self.mergesort(nums)
        return nums

    def mergesort(self, nums):
        n = len(nums)
        if n > 1:
            list1 = self.mergesort(nums[:n/2])
            list2 = self.mergesort(nums[n/2:])
            nums = self.merge(list1, list2)
        return nums

    def merge(self, list1, list2):
        sorted_list = []
        while list1 and list2:
            if list1[0] <= list2[0]:
                sorted_list.append(list1.pop(0))
            else:
                sorted_list.append(list2.pop(0))
        if not list1:
            sorted_list.extend(list2)
        if not list2:
            sorted_list.extend(list1)
        return sorted_list
