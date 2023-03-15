# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCompleteTree(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True

        queue = deque([root])
        found_gap = False

        while queue:
            node = queue.popleft()

            if found_gap and (node.left or node.right):
                return False

            if node.left:
                if found_gap and not node.right:
                    return False
                queue.append(node.left)
            else:
                found_gap = True

            if node.right:
                if found_gap:
                    return False
                queue.append(node.right)
            else:
                found_gap = True

            # Дополнительная проверка наличия потомков следующего узла в очереди
            if queue and not (node.left and node.right):
                next_node = queue[0]
                if next_node.left or next_node.right:
                    found_gap = True

        return True


# Создается функция isCompleteTree, которая принимает один аргумент root - корень бинарного дерева, представленного объектом TreeNode.

# Создается очередь queue, которая будет использоваться для обхода всех узлов дерева.

# Создается флаг found_gap, который изначально равен False и будет использоваться для отслеживания наличия пропущенных узлов.

# Итерируемся по узлам дерева в цикле while queue, пока очередь не опустеет.

# Извлекаем первый элемент очереди методом pop(0). Это узел node, который будет проверяться на соответствие условиям полноты бинарного дерева.

# Если found_gap равен True и у текущего узла есть хотя бы один потомок, то возвращаем False, потому что это не полное бинарное дерево. Это происходит потому, что в полном бинарном дереве пропуск узлов возможен только на последнем уровне, а все узлы на последнем уровне должны быть листьями.

# Если у узла есть левый потомок, то добавляем его в очередь. Если found_gap равен True и у текущего узла есть левый потомок, но нет правого, то возвращаем False, потому что это не полное бинарное дерево.

# Если у узла есть правый потомок, то добавляем его в очередь. Если found_gap равен True и у текущего узла есть правый потомок, то возвращаем False, потому что это не полное бинарное дерево.

# Если found_gap равен True и у текущего узла нет потомков (т.е. он является листовым узлом), то продолжаем обход очереди, потому что еще могут быть листовые узлы в очереди.

# Если у узла есть оба потомка, то добавляем их в очередь для дальнейшего обхода.

# Если у узла нет потомков, то обозначаем, что найден первый пропущенный узел, устанавливая found_gap в True.

# Если очередь пуста и мы не вернули False раньше, то это полное бинарное дерево, поэтому возвращаем True.
