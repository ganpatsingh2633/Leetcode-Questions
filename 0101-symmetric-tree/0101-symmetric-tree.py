# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# class Solution:
#     def isSymmetric(self, root: TreeNode | None) -> bool:
#         if not root:
#             return True
#         def traversleft(root) :
#             if not root:
#                 return [None]
#             return  [root.val] +traversleft(root.left) +  traversleft(root.right)
#         def traversright(root) :
#             if not root:
#                 return [None]
#             return [root.val] + traversright(root.right) +   traversright(root.left)  
#         return traversleft(root.left) == traversright(root.right)

class Solution:
    def isSymmetric(self, root: TreeNode | None) -> bool:
        def mirror(a, b):
            if a is None and b is None:
                return True
            if a is None or b is None or a.val != b.val:
                return False
            return mirror(a.left, b.right) and mirror(a.right, b.left)
        return mirror(root, root)