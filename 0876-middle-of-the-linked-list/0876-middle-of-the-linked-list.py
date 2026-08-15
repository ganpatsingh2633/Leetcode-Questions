# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(-1)
        dummy.next = head
        tail = dummy.next
        c = 0
        while tail :
            c += 1
            tail = tail.next
        tail = dummy.next
        c = (c//2) + 1
        x = 0
        while tail :
            x += 1
            if x >= c:
                return tail            
            tail = tail.next