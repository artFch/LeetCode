class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if len(s) > len(t):
            return False
        if len(s) == 0:
            return True
        g = 0
        for i in range(len(t)):
            if g <= len(s) - 1:
                print(s[g])
                if s[g] == t[i]:
                    g += 1
        return g == len(s)
