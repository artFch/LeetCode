class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        bit_arr = {}
        for i in range(len(arr)):
            bit_arr[i] = (arr[i], bin(arr[i]).count('1'))
        sorted_dict = sorted(bit_arr.items(), key=lambda x: (x[1][1], x[1][0]))
        sorted_arr = [x[1][0] for x in sorted_dict]
        return sorted_arr
