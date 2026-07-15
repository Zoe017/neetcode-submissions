# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import heapq
class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap = []
        for i, head in enumerate(lists):
            if head:
                heapq.heappush(heap, (head.val, i, head))
        dummy = ListNode()
        p = dummy
        while heap:
            val, i, node = heapq.heappop(heap)
            p.next = node
            curr = node
            curr = curr.next
            p = p.next
            if curr:
                heapq.heappush(heap, (curr.val, i, curr))
        return dummy.next

        