def make_node(key):
    return {'key': key, 'left': None, 'right': None}

def insert(root, node):
    if not root:
        root = node
    elif node['key'] < root['key']:
        if not root['left']:
            root['left'] = node
        else:
            insert(root['left'], node)
    elif node['key'] >= root['key']:
        if not root['right']:
            root['right'] = node
        else:
            insert(root['right'], node)
    # else:
    #     return

def height(root):
    if root is None:
        return 0
    left_height = height(root['left'])
    right_height = height(root['right'])

    return 1 + max(left_height, right_height)

def print_tree(root, level=0, prefix="Root:"):
    if root is not None:
        print("  " * level + prefix + f" {root['key']}")
        if root['left'] or root['right']:
            print_tree(root['left'], level + 1, "L--")
            print_tree(root['right'], level + 1, "R--")

keys = [7, 3, 2, 1, 9, 5, 4, 6, 8, 0]
root = None

for key in keys:
    if root == None:
        root = make_node(key)
    else:
        if key != 0:
            node = make_node(key)
            insert(root, node)
print_tree(root)
print(height(root))