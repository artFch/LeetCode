class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        def check(n_arr, x, y, z):
            if x + y > z and y + z > x and x + z > y:
                n_arr.append(x+y+z)

        n_arr = []
        for x in range(len(nums)):
            for y in range(x+1, len(nums)):
                for z in range(y+1, len(nums)):
                    check(n_arr, nums[x], nums[y], nums[z])
        if n_arr:
            return max(n_arr)
        else:
            return 0
