# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        arr = []
        for listing in lists:
            x = listing
            while x:
                arr += [x.val]
                x = x.next
                arr = sorted(arr, reverse=True)
        result = None
        for i in arr:
            print(i)
            result = ListNode(i, result)
        return result
