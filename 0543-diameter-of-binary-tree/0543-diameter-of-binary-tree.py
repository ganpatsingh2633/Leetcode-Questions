# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        best = 0
        def height(root):
            nonlocal best 
            if root is None:
                return 0
            leftht = height(root.left)
            rightht = height(root.right)
            best = max(best, leftht + rightht )
            return max(leftht, rightht) + 1
        height(root)
        return best
        # if root is None :
        #     return 0
        # leftH = self.diameterOfBinaryTree(root.left)
        # rightH = self.diameterOfBinaryTree(root.right)
        # curr = height(root.left) + height(root.right)
        # return max(curr , max(leftDiameter , rightDiameter))


        # best = 0
        # def height(node):
        #     nonlocal best
        #     if not node:
        #         return 0
        #     left = height(node.left)
        #     right = height(node.right)
        #     best = max(best, left + right)     # longest path through this node
        #     return 1 + max(left, right)        # height, for the parent
        # height(root)
        # return best