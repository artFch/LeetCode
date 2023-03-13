class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        for i in set(ransomNote):
            print("mag.count", i, "|", magazine.count(i))
            print("ran.count", i, "|", ransomNote.count(i))
            if magazine.count(i) < ransomNote.count(i):
                return False
        return True
