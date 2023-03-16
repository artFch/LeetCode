class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        x0, y0 = coordinates[0]
        x1, y1 = coordinates[1]
        dx, dy = x1 - x0, y1 - y0
        for i in range(2, len(coordinates)):
            xi, yi = coordinates[i]
            if dx * (yi - y0) - dy * (xi - x0) != 0:
                return False
        return True
