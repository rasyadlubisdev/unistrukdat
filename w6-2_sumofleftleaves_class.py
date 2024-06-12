class Node:
    def __init__(self, data):
        self.data = data
        self.right_child = None
        self.left_child = None

class Tree:
    def __init__(self):
        self.root_node = None
    def insert(self, data):
        node = Node(data)
        if self.root_node is None:
            self.root_node = node
            return self.root_node
        else:
            current = self.root_node
            parent = None
            while True:
                parent = current
                if node.data < parent.data:
                    current = current.left_child
                    if current is None:
                        parent.left_child = node
                        return self.root_node
                else:
                    current = current.right_child
                    if current is None:
                        parent.right_child = node
                        return self.root_node
    def sum_of_left_leaves(self, root):
        self.total = 0
        def dfs(node, left):
            if node is None:
                return
            dfs(node.left_child, True)
            dfs(node.right_child, False)
            if left and node.left_child is None and node.right_child is None:
                self.total += node.data

        dfs(root, False)
        return self.total
    
def print_tree(root, level=0, prefix="Root:"):
    if root is not None:
        print("  " * level + prefix + f" {root.data}")
        if root.left_child or root.right_child:
            print_tree(root.left_child, level + 1, "L--")
            print_tree(root.right_child, level + 1, "R--")


keys = [14, 9, 1, 14, 20, 13]
tree = Tree()

for key in keys:
    tree.insert(key)

root = Node(14)
tree.sum_of_left_leaves(root)