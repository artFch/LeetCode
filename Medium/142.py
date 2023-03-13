# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return None
        if head.next is head:
            return head
        slow = fast = head
        while fast:
            slow, fast = slow.next, fast.next.next
            if slow == fast:
                break
        slow = head
        while slow is fast:
            slow, fast = slow.next, fast.next
