# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        
        if len(lists) == 0:
            return
        while len(lists) > 1:
            mergedLists = []
            i = 0
            while i < len(lists):
                l1 = lists[i]
                l2 = lists[i + 1] if i + 1 < len(lists) else None
                mergedLists.append(self.merge(l1, l2))
                i += 2
            lists = mergedLists
        return lists[0]
    
    def merge(self, l1, l2):
        curr1 = l1
        curr2 = l2
        dummy = ListNode()
        point = dummy
        while curr1 and curr2:
            if curr1.val <= curr2.val:
                point.next = curr1
                point = point.next
                curr1 = curr1.next
            else:
                point.next = curr2
                point = point.next
                curr2 = curr2.next
        if curr1:
            point.next = curr1
        else:
            point.next = curr2
        return dummy.next