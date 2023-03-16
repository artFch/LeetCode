inorder = [9, 3, 15, 20, 7]
postorder = [9, 15, 7, 20, 3]


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def func(inorder, postorder):
    if not inorder or not postorder:
        return None
    node = TreeNode(postorder[-1])
    print(node)
    ind = inorder.index(node)
    left_in = inorder[:ind]
    right_in = inorder[ind+1:]
    left_post = postorder[:ind]
    right_post = postorder[ind:-1]
    node.left = func(inorder=left_in, postorder=left_post)
    node.right = func(inorder=right_in, postorder=right_post)
    return node
