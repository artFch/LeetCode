# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True
        else:
            return self.check(root.left, root.right)

    def check(self, left, right):
        if (left == None and right == None):
            return True
        if left is None or right is None:
            return False
        if left.val == right.val:
            outPair = self.check(left.left, right.right)
            inPair = self.check(left.right, right.left)
            return outPair and inPair
        else:
            return False
