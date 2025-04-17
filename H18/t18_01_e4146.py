class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.height = 1
def gp(node):
    return node.height if node else 0
def pp(node):
    node.height = max(gp(node.left), gp(node.right)) + 1
def b(node):
    return gp(node.right) - gp(node.left)
def g(y):
    x = y.left
    T2 = x.right
    x.right = y
    y.left = T2
    pp(y)
    pp(x)
    return x
def ss(x):
    y = x.right
    T2 = y.left
    y.left = x
    x.right = T2
    pp(x)
    pp(y)
    return y
def balance(node):
    pp(node)
    if b(node) == 2:
        if b(node.right) < 0:
            node.right = g(node.right)
        return ss(node)
    if b(node) == -2:
        if b(node.left) > 0:
            node.left = ss(node.left)
        return g(node)
    return node
def insert(node, key):
    if node is None:
        return Node(key)
    if key < node.key:
        node.left = insert(node.left, key)
    elif key > node.key:
        node.right = insert(node.right, key)
    else:
        return node
    return balance(node)
def find_min(node):
    return node if node.left is None else find_min(node.left)
def remove_min(node):
    if node.left is None:
        return node.right
    node.left = remove_min(node.left)
    return balance(node)
def delete(node, key):
    if node is None:
        return None
    if key < node.key:
        node.left = delete(node.left, key)
    elif key > node.key:
        node.right = delete(node.right, key)
    else:
        l = node.left
        r = node.right
        if r is None:
            return l
        min_node = find_min(r)
        min_node.right = remove_min(r)
        min_node.left = l
        return balance(min_node)
    return balance(node)
def exists(node, key):
    if node is None:
        return False
    if key < node.key:
        return exists(node.left, key)
    elif key > node.key:
        return exists(node.right, key)
    else:
        return True
root = None
while True:
    try:
        line = input()
    except EOFError:
        break
    if not line:
        break
    parts = line.split()
    if not parts:
        continue
    cmd = parts[0]
    x = int(parts[1])
    if cmd == "insert":
        root = insert(root, x)
    elif cmd == "delete":
        root = delete(root, x)
    elif cmd == "exists":
        print("true" if exists(root, x) else "false")