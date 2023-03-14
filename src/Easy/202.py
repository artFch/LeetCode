class Solution:
    def isHappy(self, n: int) -> bool:
        slow = n
        fast = n

        while True:
            slow = self.happy(slow)
            fast = self.happy(self.happy(fast))

            if slow == fast:
                break

        return slow == 1

    def happy(self, n: int) -> int:
        sum = 0
        while n > 0:
            digit = n % 10
            sum += digit * digit
            n //= 10
        return sum
