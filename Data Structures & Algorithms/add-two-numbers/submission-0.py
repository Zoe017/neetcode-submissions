# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        def s(node):
            if not node.next:
                return node.val
            return node.val + s(node.next) * 10
        total = s(l1) + s(l2)
        if total == 0:
            return ListNode(0)
        def new(total):
            if total == 0:
                return
            return ListNode(total % 10, new(total // 10))
        return new(total)