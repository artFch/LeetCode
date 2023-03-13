class Solution:
    def preorder(self, root: 'Node') -> list[int]:
        output = []

        self.dfs(root, output)

        return output

    def dfs(self, root, output):
        if root == None:
            return
        output.append(root.val)

        for child in root.children:
            self.dfs(child, output)
