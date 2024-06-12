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
total = 0
def sum_of_left_leaves(root):

    def dfs(node, left):
        global total
        if node is None:
            return
        dfs(node['left'], True)
        dfs(node['right'], False)
        if left and node['left'] is None and node['right'] is None:
            total += node['key']

    dfs(root, False)
    return total
    

def print_tree(root, level=0, prefix="Root:"):
    if root is not None:
        print("  " * level + prefix + f" {root['key']}")
        if root['left'] or root['right']:
            print_tree(root['left'], level + 1, "L--")
            print_tree(root['right'], level + 1, "R--")

keys = [14, 9, 1, 14, 20, 13, 19]
root = None

for key in keys:
    if root == None:
        root = make_node(key)
    else:
        node = make_node(key)
        insert(root, node)
print_tree(root)
print(sum_of_left_leaves(root))