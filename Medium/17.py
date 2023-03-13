class Solution:
    def letterCombinations(self, digits: str) -> list[str]:
        if not digits or "0" in digits or "1" in digits:
            return
        map = {
            "2": ["a", "b", "c"],
            "3": ["d", "e", "f"],
            "4": ["g", "h", "i"],
            "5": ["j", "k", "l"],
            "6": ["m", "n", "o"],
            "7": ["p", "q", "r", "s"],
            "8": ["t", "u", "v"],
            "9": ["w", "x", "y", "z"]
        }
        print(digits[0])
        i = 1
        output = map[digits[0]]
        while i < len(digits):
            next = []
            for j in output:
                for k in map[digits[i]]:
                    next.append(j+k)
            output = next
            i += 1
        return output
