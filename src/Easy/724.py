class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        leftSum, rightSum = 0, sum(nums)
        for i in range(len(nums)):
            rightSum -= nums[i]
            if rightSum == leftSum:
                #print(i)
                return i
            leftSum += nums[i]
        #print(-1)
        return -1
