class Solution:
    def minimumTime(self, time: list[int], totalTrips: int) -> int:
        r = totalTrips * min(time)+1
        l = 0
        t = 0

        def check_status(expected_time: int) -> int:
            nonlocal t
            count = 0
            for i in time:
                count += expected_time // i
            if count < totalTrips:
                return 1  # Since number of trips are less then required, left moves to mid
            elif count >= totalTrips:
                t = expected_time
                return -1

        while l < r-1:  # Till Binary Search can continue.
            mid = (l + r) // 2
            status = check_status(mid)
            if status == 1:
                l = mid
            else:
                r = mid
        return t
