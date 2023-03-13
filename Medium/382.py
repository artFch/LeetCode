import random
import math


class Solution:

    def __init__(self, head: Optional[ListNode]):
        self.head = head

    def getRandom(self) -> int:
        curr = self.head
        res = None
        count = 0
        while curr:
            count += 1
            if random.randint(1, count) == 1:
                res = curr.val
            curr = curr.next

        return res


# class Solution:

#     def __init__(self, head: Optional[ListNode]):
#         nodes = []
#         curr = head
#         while curr:
#             nodes.append(curr)
#             curr = curr.next
#         self.nodes = nodes

#     def getRandom(self) -> int:
#         i = math.floor(random.random() * len(self.nodes))
#         return self.nodes[i].val
