class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        l1 = len(word1)
        l2 = len(word2)
        n = min(l1, l2)
        result = ""
        for i in range(n):
            result += word1[i]
            result += word2[i]
        if l1 > l2:
            result += word1[l2:]
        else:
            result += word2[l1:]
        return result
