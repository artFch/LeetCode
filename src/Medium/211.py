class TrieNode:
    def __init__(self):
        self.children = {}
        self.isWordCompleted = False


class WordDictionary:
    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        curr_node = self.root
        for symb in word:
            if symb not in curr_node.children:
                curr_node.children[symb] = TrieNode()
            curr_node = curr_node.children[symb]
        curr_node.isWordCompleted = True

    def search(self, word: str) -> bool:
        def recursive(node, i):
            if i == len(word):
                return node.isWordCompleted
            symb = word[i]
            if symb == ".":
                for child in node.children.values():
                    if recursive(child, i+1):
                        return True
                return False
            if word[i] in node.children:
                return recursive(node.children[symb], i+1)
            return False
        return recursive(self.root, 0)
