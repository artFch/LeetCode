class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        a = sorted(arr)
        difference = a[1] - a[0]
        for i in range(2, len(a)):
            if a[i] - a[i-1] != difference:
                return False
        return True
