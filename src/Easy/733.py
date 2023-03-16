class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        replace_color = image[sr][sc]
        rows, cols = len(image), len(image[0])

        def func(image, sr, sc):
            if sr <= 0 or sr >= rows or sc <= 0 or sc >= cols:
                return
            if replace_color == image[sr][sc]:
                return
            if replace_color != image[sr][sc] or image[sr][sc] == color:
                return
            image[sr][sc] = color
            # up
            func(image, sr-1, sc)
            # down
            func(image, sr+1, sc)
            # right
            func(image, sr, sc+1)
            # left
            func(image, sr+1, sc-1)

        func(image, sr, sc)
        return image
