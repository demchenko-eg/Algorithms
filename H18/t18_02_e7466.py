class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
class Tree:
    def __init__(self):
        self.head = None
    def Insert(self, val):
        self.head = self._insert(self.head, val)
    def _insert(self, node, val):
        if node is None:
            return TreeNode(val)
        if val < node.val:
            node.left = self._insert(node.left, val)
        else:
            node.right = self._insert(node.right, val)
        return node
    def IsBalanced(self):
        return 1 if self._is_balanced(self.head)[0] else 0
    def _is_balanced(self, node):
        if node is None:
            return True, 0
        lb, lh = self._is_balanced(node.left)
        rb, rh = self._is_balanced(node.right)
        balanced = lb and rb and abs(lh - rh) <= 1
        return balanced, max(lh, rh) + 1
n = int(input())
tree = Tree()
for x in map(int, input().split()):
    tree.Insert(x)
print(tree.IsBalanced())