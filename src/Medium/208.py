class TrieNode:
    def __init__(self):
        self.children = {}
        self.isWordCompleted = False


class Trie:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        curr_node = self.root
        for symb in word:
            if symb not in curr_node.children:
                curr_node.children[symb] = TrieNode()
            curr_node = curr_node.children[symb]
        curr_node.isWordCompleted = True

    def search(self, word: str) -> bool:
        curr_node = self.root
        for symb in word:
            if symb not in curr_node.children:
                return False
            curr_node = curr_node.children[symb]
        return curr_node.is_end_of_word

    def startsWith(self, prefix: str) -> bool:
        curr_node = self.root
        for symb in prefix:
            if symb in curr_node.children:
                curr_node = curr_node.children[symb]
            else:
                return False
        return True
        # Your Trie object will be instantiated and called as such:
        # obj = Trie()
        # obj.insert(word)
        # param_2 = obj.search(word)
        # param_3 = obj.startsWith(prefix)
