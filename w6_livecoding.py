from collections import deque

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
    elif node['key'] > root['key']:
        if not root['right']:
            root['right'] = node
        else:
            insert(root['right'], node)
    else:
        return

def search(root, value):
    while root:
        if value["key"] > root['key']:
            root = root['right']
        elif value["key"] < root['key']:
            root = root['left']
        else:
            return root
    return None

def find(root, value):
    temp = search(root, value)
    if temp == None:return False
    if temp['key'] == value: return True
    else: return False

def find_min(node):
    current = node
    while current and current['left']:
        current = current['left']
    return current

def find_max(node):
    current = node
    while current and current['right']:
        current = current['right']
    return current

def remove(root, value):
    if root == None: return root
    if value < root['key']:
        root['left'] = remove(root['left'], value)
    elif value > root['key']:
        root['right'] = remove(root['right'], value)
    else:
        if root['left'] == None:
            temp = root['right']
            root = None
            return temp
        elif root['right'] == None:
            temp = root['left']
            root = None
            return temp
        temp = find_min(root['right'])
        root['key'] = temp['key']
        root['right'] = remove(root['right'], temp['key'])
    return root

def pre_order(root):
    if root:
        print(root['key'])
        pre_order(root['left'])
        pre_order(root['right'])

def in_order(root):
    if root:
        in_order(root['left'])
        print(root['key'])
        in_order(root['right'])

def post_order(root):
    if root:
        post_order(root['left'])
        post_order(root['right'])
        print(root['key'])

def level_order(root):
    if not root:
        return

    queue = deque([root])

    while queue:
        current_node = queue.popleft()
        print(current_node['key'])

        if current_node['left']:
            queue.append(current_node['left'])
        if current_node['right']:
            queue.append(current_node['right'])

def print_tree(root, level=0, prefix="Root:"):
    if root is not None:
        print("  " * level + prefix + f" {root['key']}")
        if root['left'] or root['right']:
            print_tree(root['left'], level + 1, "L--")
            print_tree(root['right'], level + 1, "R--")

# keys = [7, 5, 12, 3, 6, 9, 15, 1, 4, 8, 10, 13, 17]
# root = None

# print("=== 1. make_node ===")
# for key in keys:
#     if root == None:
#         root = make_node(key)
#     else:
#         node = make_node(key)
#         insert(root, node)
# print_tree(root)


#ngerjain soal

N = int(input())
keys = [int(x) for x in input().split()]
print(keys)
root = None
for key in keys:
    if root == None:
        root = make_node(key)
    else:
        node = make_node(key)
        insert(root, node)

T = int(input())
for _ in range(T):
    new_input = input().split()
    strng = new_input[0]

    if strng == "insert":
        value = make_node(int(new_input[1]))
        # print(root)
        # print(value)
        if not find(root, value):
            insert(root, value)
    elif strng == "remove":
        value = make_node(int(new_input[1]))
        if not find(root, value):
            remove(root, value)
    elif strng == "inorder":
        in_order(root)
    elif strng == "preorder":
        pre_order(root)
    elif strng == "postorder":
        post_order(root)
    else:
        print("Salah input")
        break

