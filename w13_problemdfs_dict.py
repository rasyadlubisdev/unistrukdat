def make_node(key):
    return {'key': key, 'left': None, 'right': None} if key is not None else None

def insert_level_order(arr, root, i, n):
    if i < n:
        temp = make_node(arr[i])
        root = temp

        if root is not None:
            root['left'] = insert_level_order(arr, root['left'], 2 * i + 1, n)
            root['right'] = insert_level_order(arr, root['right'], 2 * i + 2, n)
    return root

def hasPathSum(root, targetSum):
    if not root:
        return False
    
    if not root['left'] and not root['right'] and root['key'] == targetSum:
        return True
    
    return hasPathSum(root['left'], targetSum - root['key']) or hasPathSum(root['right'], targetSum - root['key'])

def print_tree(root, level=0, prefix="Root:"):
    if root is not None:
        print("  " * level + prefix + f" {root['key']}")
        if root['left'] or root['right']:
            print_tree(root['left'], level + 1, "L--")
            print_tree(root['right'], level + 1, "R--")

keys_1 = [5, 4, 8, 11, None, 13, 4, 7, 2, None, None, None, 1]
root_1 = None
root_1 = insert_level_order(keys_1, None, 0, len(keys_1))
print(hasPathSum(root_1, 22))

keys_2 = [1, 2, 3]
root_2 = None
root_2 = insert_level_order(keys_2, None, 0, len(keys_2))
print(hasPathSum(root_2, 5))

# print_tree(root)
