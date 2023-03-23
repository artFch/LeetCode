class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        dictionary = {}
        for i in range(len(order)):
            dictionary[order[i]] = i

        def compare_words(w1, w2):
            for c1, c2 in zip(w1, w2):
                if dictionary[c1] < dictionary[c2]:
                    return True
                elif dictionary[c1] > dictionary[c2]:
                    return False
            return len(w1) <= len(w2)

        for i in range(len(words)-1):
            if not compare_words(words[i], words[i+1]):
                return False

        return True
