# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        curr = head
        if not curr.next or not curr.next.next:
            return
        while curr and curr.next:
            last = curr
            while last.next:
                prev = last
                last = last.next
            prev.next = None
            
            temp = curr.next
            curr.next = last
            last.next = temp
            curr = curr.next.next
        return None