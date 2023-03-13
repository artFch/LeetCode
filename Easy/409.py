import collections as col


class Solution:
    def longestPalindrome(self, s: str) -> int:
        letters = col.Counter(s)
        result = 0
        odd = 0
        if len(letters) == 1:
            print(len(s))
        for i in letters.values():
            if i > 1:
                if i % 2 == 0:
                    result += i
                else:
                    result += i-1
                    odd += 1
            else:
                odd += 1
        if odd > 0:
            result += 1
        return result
