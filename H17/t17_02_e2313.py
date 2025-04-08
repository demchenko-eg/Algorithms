import sys
sys.setrecursionlimit(1500)
class Node:
    def __init__(self, v):
        self.v = v
        self.l = None
        self.r = None

def insert(root, v):
    if root is None:
        return Node(v)
    if v < root.v:
        root.l = insert(root.l, v)
    elif v > root.v:
        root.r = insert(root.r, v)
    return root

def count(root):
    if root is None:
        return 0
    return count(root.l) + count(root.r) + 1

a = []
try:
    while True:
        a.extend(list(map(int, input().split())))
except:
    pass
root = None
for x in a:
    if x == 0:
        break
    root = insert(root, x)
print(count(root))