class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        n = len(mat)
        summ = 0
        for i in range(n):
            for j in range(n):
                if i == j:
                    summ += mat[i][j]
                elif i + j == n - 1:
                    summ += mat[i][j]
        return summ
