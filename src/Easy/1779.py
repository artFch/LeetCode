class Solution:
    def nearestValidPoint(self, x: int, y: int, points: List[List[int]]) -> int:
        INF = sys.maxsize

        def m_distance(x1, y1, x2, y2):
            if x1 == x2 or y1 == y2:
                n_arr.append(abs(x1 - x2) + abs(y1 - y2))
            else:
                n_arr.append(INF)

        n_arr = []

        for i in points:
            m_distance(x, y, i[0], i[1])

        if n_arr:
            min_value = min(n_arr)
            print(n_arr)
            if min_value == INF:
                return -1
            else:
                return n_arr.index(min_value)
        else:
            return -1
