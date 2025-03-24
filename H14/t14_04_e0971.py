# n = 10, k = 3
# 3 > 6 > 9 > 2 > 7 > 1 > 8 > 5 > 10 > 4

class Queue:
    def __init__(self):
        self.items = []
    # def empty(self):
    #     return len(self.items) == 0
    def push(self, item):
        self.items.append(item)
    def pop(self):
        return self.items.pop(0)
    def front(self):
        return self.items[0]
    def size(self):
        return len(self.items)

n, k = map(int, input().split())
q = Queue()
for i in range(1, n + 1):
    q.push(i)
while q.size() > 1:
    for _ in range(k - 1):
        q.push(q.pop())
    q.pop()
print(q.front())