# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        def length(head):
            count = 0
            current_node = head
            while current_node:
                count += 1
                current_node = current_node.next
            return count

        result = 0
        i = length(head) - 1
        print(i)
        curr_node = head
        while curr_node:
            result += curr_node.val * pow(2, i)
            curr_node = curr_node.next
            i -= 1
        return result
