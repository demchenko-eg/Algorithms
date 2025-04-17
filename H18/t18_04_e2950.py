class TreeNode:
    def __init__(self, idx, color):
        self.idx = idx
        self.color = color
        self.left = None
        self.right = None

class Tree:
    def __init__(self):
        self.head = None
        self.valid = True
    def Build(self, n, nodes_info):
        nodes = [None]*(n+1)
        for i in range(1, n+1):
            p, col = nodes_info[i-1]
            nodes[i] = TreeNode(i, col)
        for i in range(1, n+1):
            p, _ = nodes_info[i-1]
            if p == -1:
                self.head = nodes[i]
            else:
                if nodes[p].left is None:
                    nodes[p].left = nodes[i]
                else:
                    nodes[p].right = nodes[i]
        self.nodes = nodes
    def CheckRedBlack(self):
        if self.head.left is None and self.head.right is None and self.head.color != 'B':
            self.valid = False
        def dfs(node):
            if node is None:
                return 1
            if (node.left is None and node.right is not None) or (node.left is not None and node.right is None):
                self.valid = False
                return 0
            if node.left is None and node.right is None:
                if node.color != 'B':
                    self.valid = False
                return 1
            if node.left and node.right:
                if node.color == 'R':
                    if node.left.color == 'R':
                        self.valid = False
                    if node.right.color == 'R':
                        self.valid = False
                lb = dfs(node.left)
                rb = dfs(node.right)
                if lb != rb:
                    self.valid = False
                return lb + (1 if node.color == 'B' else 0)
        dfs(self.head)
    def Build234(self):
        rep = {}
        def assign(node, cur):
            cur = node.idx if cur is None or node.color == 'B' else cur
            rep[node.idx] = cur
            if node.left:
                assign(node.left, cur)
            if node.right:
                assign(node.right, cur)
        assign(self.head, None)
        edges = set()
        def collect(node):
            if node.left:
                if rep[node.idx] != rep[node.left.idx]:
                    edges.add((rep[node.idx], rep[node.left.idx]))
                collect(node.left)
            if node.right:
                if rep[node.idx] != rep[node.right.idx]:
                    edges.add((rep[node.idx], rep[node.right.idx]))
                collect(node.right)
        collect(self.head)
        return edges

n = int(input())
nodes_info = [tuple(input().split()) for _ in range(n)]
nodes_info = [(int(p), c) for p, c in nodes_info]
tree = Tree()
tree.Build(n, nodes_info)
tree.CheckRedBlack()
if not tree.valid:
    print("NO")
else:
    ed = tree.Build234()
    edges = sorted(list(ed), key=lambda x: (x[0], x[1]))
    print("YES")
    print(len(edges))
    for u, v in edges:
        print(u, v)