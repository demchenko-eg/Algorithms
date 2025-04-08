class Node:
    def __init__(self, v):
        self.v = v
        self.l = None
        self.r = None

    def insert(self, v):
        if v < self.v:
            if self.l is None:
                self.l = Node(v)
            else:
                self.l.insert(v)
        elif v > self.v:
            if self.r is None:
                self.r = Node(v)
            else:
                self.r.insert(v)

def u(nums, i, l, j):
    if i == len(nums):
        return True
    curr = nums[i]
    if not (l < curr < j):
        return False
    if i == len(nums) - 1:
        return True
    nextv = nums[i + 1]
    if nextv < curr:
        return u(nums, i + 1, l, curr)
    else:
        return u(nums, i + 1, curr, j)

def rg(nums):
    return u(nums, 0, -float('inf'), float('inf'))

iput = ""
while True:
    try:
        line = input()
    except EOFError:
        break
    if line == "":
        continue
    iput += line + " "
iput = iput.strip()
if not iput:
    print("NO")
try:
    nums = list(map(int, iput.split()))
except Exception:
    print("NO")
if rg(nums):
    print("YES")
else:
    print("NO")