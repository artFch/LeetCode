class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dictionary = {}
        for i in s:
            if i in dictionary:
                dictionary[i] += 1
            else:
                dictionary[i] = 1
        for j in t:
            if j in dictionary:
                dictionary[j] -= 1
            else:
                return False
        for i in s:
            if dictionary[i] != 0:
                return False
        print(dictionary)
        return True
