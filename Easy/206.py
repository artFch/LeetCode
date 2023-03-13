# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        while head:
            curr = head
            head = head.next
            curr.next = prev
            prev = curr
        return prev
#     none - 1 - 2 - 3 - 4
# prev  |
# head       |
# cur        |
# while
#     none - 1 - 2 - 3 - 4        0 сurr.next = None, None
# prev       |
# head           |
# cur        |
#     none - 1 - 2 - 3 - 4        1 curr.next = 1, 1 -> None
# prev           |
# head               |
# cur            |
#     none - 1 - 2 - 3 - 4        1 curr.next = 2, 2 -> 1 -> None
# prev               |
# head                   |
# cur                |
#     none - 1 - 2 - 3 - 4        1 curr.next = 2, 2 -> 1 -> None
# prev               |
# head                   |
# cur                    |
