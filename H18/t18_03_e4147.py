class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.height = 1
        self.size = 1

def get_height(node):
    return node.height if node else 0

def get_size(node):
    return node.size if node else 0

def recalc(node):
    node.height = max(get_height(node.left), get_height(node.right)) + 1
    node.size = get_size(node.left) + get_size(node.right) + 1

def balance_factor(node):
    return get_height(node.right) - get_height(node.left)

def rotate_right(y):
    x = y.left
    y.left = x.right
    x.right = y
    recalc(y)
    recalc(x)
    return x

def rotate_left(x):
    y = x.right
    x.right = y.left
    y.left = x
    recalc(x)
    recalc(y)
    return y

def balance(node):
    recalc(node)
    if balance_factor(node) == 2:
        if balance_factor(node.right) < 0:
            node.right = rotate_right(node.right)
        return rotate_left(node)
    if balance_factor(node) == -2:
        if balance_factor(node.left) > 0:
            node.left = rotate_left(node.left)
        return rotate_right(node)
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

def delete(node, key):
    if node is None:
        return None
    if key < node.key:
        node.left = delete(node.left, key)
    elif key > node.key:
        node.right = delete(node.right, key)
    else:
        if node.left is None:
            return node.right
        if node.right is None:
            return node.left
        min_node = find_min(node.right)
        node.key = min_node.key
        node.right = delete(node.right, min_node.key)
    return balance(node) if node else None

def exists(node, key):
    if node is None:
        return False
    if key < node.key:
        return exists(node.left, key)
    elif key > node.key:
        return exists(node.right, key)
    else:
        return True

def next_val(node, key):
    result = None
    while node:
        if node.key > key:
            result = node.key
            node = node.left
        else:
            node = node.right
    return result

def prev_val(node, key):
    result = None
    while node:
        if node.key < key:
            result = node.key
            node = node.right
        else:
            node = node.left
    return result

def kth(node, k):
    if node is None:
        return None
    left_size = get_size(node.left)
    if k == left_size + 1:
        return node.key
    elif k <= left_size:
        return kth(node.left, k)
    else:
        return kth(node.right, k - left_size - 1)

root = None
while True:
    try:
        line = input()
    except EOFError:
        break
    if not line:
        break
    parts = line.split()
    op = parts[0]
    x = int(parts[1])
    if op == "insert":
        root = insert(root, x)
    elif op == "delete":
        root = delete(root, x)
    elif op == "exists":
        print("true" if exists(root, x) else "false")
    elif op == "next":
        res = next_val(root, x)
        print(res if res is not None else "none")
    elif op == "prev":
        res = prev_val(root, x)
        print(res if res is not None else "none")
    elif op == "kth":
        res = kth(root, x)
        print(res if res is not None else "none")