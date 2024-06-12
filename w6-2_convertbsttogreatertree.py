# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def convertBST(self, root):
        def in_order(node, total):
            if node:
                total = in_order(node.right, total)

                total += node.val
                node.val = total

                total = in_order(node.left, total)

            return total
        
        in_order(root, 0)
        return root
        