# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDiffInBST(self, root: TreeNode | None) -> int:
        res = float('inf')
        pre  = -1 
        def mindiff(root):
            nonlocal res, pre
            if not root :
                return 
            if root.left != None:
                mindiff(root.left)
            if pre >= 0:
                res = min(res , root.val - pre)
            pre = root.val
            if root.right != None:
                mindiff(root.right)
        mindiff(root)
        return int(res)

# class Solution:
#     def minDiffInBST(self, root: TreeNode | None) -> int:
#         res = float('inf')
#         pre = -1  # Initialized as an integer, not a string
        
#         def mindiff(node):
#             nonlocal res, pre  # Allows modifying variables from the outer scope
            
#             if not node:
#                 return
            
#             # 1. Traverse the left subtree
#             mindiff(node.left)
            
#             # 2. Process the current node
#             if pre >= 0:
#                 res = min(res, node.val - pre)
#             pre = node.val  # Update the previous node value
            
#             # 3. Traverse the right subtree
#             mindiff(node.right)
            
#         mindiff(root)
#         return int(res)
