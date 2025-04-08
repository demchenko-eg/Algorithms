class Node:
    def __init__(self, v):
        self.v = v
        self.l = None
        self.r = None

def ik(sl, g, low, high):
    if low > high:
        return None
    best = low
    for i in range(low, high + 1):
        if g[sl[i]] > g[sl[best]]:
            best = i
    root = Node(sl[best])
    root.l = ik(sl, g, low, best - 1)
    root.r = ik(sl, g, best + 1, high)
    return root

def iv(node):
    if node is None:
        return ""
    return node.v + iv(node.l) + iv(node.r)

rounds = []
while True:
    line = input().strip()
    if line == "*":
        break
    if line:
        rounds.append("".join(line.split()))
g = {}
for i, s in enumerate(rounds, start=1):
    for ch in s:
        g[ch] = i
if not g:
    print("")
lts = list(g.keys())
lts.sort()
root = ik(lts, g, 0, len(lts) - 1)
print(iv(root))