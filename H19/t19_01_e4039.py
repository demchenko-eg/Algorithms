class Heap:
    def __init__(self):
        self.mItems = [0]
        self.mSize = 0

    def insert(self, key):
        self.mSize += 1
        self.mItems.append(key)
        self.siftUp()

    def siftUp(self):
        i = len(self.mItems) - 1
        while i > 1:
            parent = i // 2
            if self.mItems[i] > self.mItems[parent]:
                self.swap(parent, i)
                i = parent
            else:
                break

    def extractMaximum(self):
        root = self.mItems[1]
        self.mItems[1] = self.mItems[-1]
        self.mItems.pop()
        self.mSize -= 1
        self.siftDown()
        return root

    def siftDown(self):
        i = 1
        while 2 * i <= self.mSize:
            left = 2 * i
            right = 2 * i + 1
            max_child = self.maxChild(left, right)
            if self.mItems[i] < self.mItems[max_child]:
                self.swap(max_child, i)
                i = max_child
            else:
                break

    def swap(self, i, j):
        self.mItems[i], self.mItems[j] = self.mItems[j], self.mItems[i]

    def maxChild(self, left_child, right_child):
        if right_child > self.mSize:
            return left_child
        else:
            if self.mItems[left_child] > self.mItems[right_child]:
                return left_child
            else:
                return right_child

heap = Heap()
n = int(input())
result = []
for _ in range(n):
    parts = input().split()
    if parts[0] == '0':
        heap.insert(int(parts[1]))
    else:
        result.append(str(heap.extractMaximum()))
print('\n'.join(result))