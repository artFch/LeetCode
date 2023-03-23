class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        reshape = []
        result = []
        for row in mat:
            for number in row:
                reshape.append(number)
        print(reshape)
        if r * c != len(reshape):
            return mat
        else:
            for i in range(r):
                result.append(reshape[i*c: i*c + c])
        return result
