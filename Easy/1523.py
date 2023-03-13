# def count(low, high):
#     result = 0
#     for i in range(low, high+1):
#         if not i % 2 == 0:
#             result += 1
#     return (high + 1)//2 - low//2


# def main():
#     low = 3
#     high = 7
#     print(count(low, high))


# main()
class Solution:
    def countOdds(self, low: int, high: int) -> int:
        return (high + 1)//2 - low//2
