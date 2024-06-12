class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def build_tree(elements):
    if not elements or elements[0] is None:
        return None

    root = TreeNode(elements[0])

    queue = [root]
    i = 1

    while queue and i < len(elements):
        node = queue.pop(0)
        if elements[i] is not None:
            node.left = TreeNode(elements[i])
            queue.append(node.left)
        i += 1

        if i < len(elements) and elements[i] is not None:
            node.right = TreeNode(elements[i])
            queue.append(node.right)
        i += 1

    return root


def hasPathSum(root, targetSum):
    if not root:
        return False
    
    if not root.left and not root.right and root.val == targetSum:
        return True
    
    return hasPathSum(root.left, targetSum - root.val) or hasPathSum(root.right, targetSum - root.val)

# root = TreeNode(5)
# root.left = TreeNode(4)
# root.left.left = TreeNode(11)
# root.left.left.left = TreeNode(7)
# root.left.left.right = TreeNode(2)
# root.right = TreeNode(8)
# root.right.left = TreeNode(13)
# root.right.right = TreeNode(4)
# root.right.right.right = TreeNode(1)
elements = [5, 4, 8, 11, None, 13, 4, 7, 2, None, None, None, 1]
root = build_tree(elements)

print(hasPathSum(root, 22))
