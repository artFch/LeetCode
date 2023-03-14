# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        INF = sys.maxsize

        def is_bst(node, min_value, max_value):
            # Проверяем, является ли дерево пустым
            if node is None:
                return True

            # Проверяем, что значение в корне находится в допустимом диапазоне
            if node.val < min_value or node.val > max_value:
                return False

            # Рекурсивно проверяем левое поддерево, где все значения должны быть меньше значения в корне
            if not is_bst(node.left, min_value, node.val - 1):
                return False

            # Рекурсивно проверяем правое поддерево, где все значения должны быть больше значения в корне
            if not is_bst(node.right, node.val + 1, max_value):
                return False

            # Если все условия выполнены, то это бинарное дерево поиска
            return True
        return is_bst(node=root, min_value=-INF, max_value=INF)
