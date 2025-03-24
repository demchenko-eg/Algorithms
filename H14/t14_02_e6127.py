class Node:
    def __init__(self, item):
        self.item = item
        self.next = None

class Queue:
    def __init__(self):
        self.front1 = None
    def empty(self):
        return self.front1 is None
    def push(self, item):
        if self.empty():
            self.front1 = Node(item)
        else:
            self._push(self.front1, item)
        return "ok"
    def _push(self, node, item):
        if node.next is None:
            node.next = Node(item)
        else:
            self._push(node.next, item)
    def pop(self):
        if self.empty():
            return "error"
        res = self.front1.item
        self.front1 = self.front1.next
        return res
    def front(self):
        if self.empty():
            return "error"
        return self.front1.item
    def size(self):
        return self._size(self.front1)
    def _size(self, node):
        if node is None:
            return 0
        return 1 + self._size(node.next)
    def clear(self):
        self.front1 = None
        return "ok"

q = Queue()
while True:
    cmd = input().split()
    if cmd[0] == "push":
        print(q.push(int(cmd[1])))
    elif cmd[0] == "pop":
        print(q.pop())
    elif cmd[0] == "front":
        print(q.front())
    elif cmd[0] == "size":
        print(q.size())
    elif cmd[0] == "clear":
        print(q.clear())
    elif cmd[0] == "exit":
        print("bye")
        break