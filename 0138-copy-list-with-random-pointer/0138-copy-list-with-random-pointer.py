"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""
class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None
        cur = head
        h = {None : None}
        while cur != None:
            new = Node(cur.val)
            h[cur] = new
            cur = cur.next
        cur = head
        while cur != None :
            copy = h[cur]
            copy.next = h[cur.next]
            copy.random = h[cur.random]
            cur = cur.next
        return h[head]

















        # # Step 1: Interleave cloned nodes
        # curr = head
        # while curr:
        #     new_node = Node(curr.val)
        #     new_node.next = curr.next
        #     curr.next = new_node
        #     curr = new_node.next
            
        # # Step 2: Connect random pointers
        # curr = head
        # while curr:
        #     if curr.random:
        #         curr.next.random = curr.random.next
        #     curr = curr.next.next
            
        # # Step 3: Unweave the interleaved lists
        # curr = head
        # dummy = Node(0)
        # copy_curr = dummy
        
        # while curr:
        #     # Extract the copy node
        #     copy_curr.next = curr.next
        #     copy_curr = copy_curr.next
            
        #     # Restore the original node link
        #     curr.next = curr.next.next
        #     curr = curr.next
            
        # return dummy.next