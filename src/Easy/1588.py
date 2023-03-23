class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        summ = 0
        for i in range(len(arr)):
            for j in range(i, len(arr), 2):
                summ += sum(arr[i:j+1])
        return summ
