class Node:
    def __init__(self, value, prev=None, next=None):
        self.value = value
        self.prev = prev
        self.next = next

class Deque:
    def __init__(self, head=None, tail=None, size=0):
        self.head = head
        self.tail = tail
        self._size = size

    def push_front(self, value):
        new_node = Node(value, next=self.head)
        if self.head is None:
            return Deque(new_node, new_node, self._size + 1)
        self.head.prev = new_node
        return Deque(new_node, self.tail, self._size + 1)

    def push_back(self, value):
        new_node = Node(value, prev=self.tail)
        if self.tail is None:
            return Deque(new_node, new_node, self._size + 1)
        self.tail.next = new_node
        return Deque(self.head, new_node, self._size + 1)

    def pop_front(self):
        if self.head is None:
            return None, self
        new_head = self.head.next
        if new_head is not None:
            new_head.prev = None
        return self.head.value, Deque(new_head, self.tail if new_head else None, self._size - 1)

    def pop_back(self):
        if self.tail is None:
            return None, self
        new_tail = self.tail.prev
        if new_tail is not None:
            new_tail.next = None
        return self.tail.value, Deque(self.head if new_tail else None, new_tail, self._size - 1)

    def front(self):
        return self.head.value if self.head else None

    def back(self):
        return self.tail.value if self.tail else None

    def size(self):
        return self._size

    def clear(self):
        return Deque()

dq = Deque()
while True:
    try:
        line = input().strip()
    except EOFError:
        break
    if not line:
        continue
    cmd = line.split()
    if cmd[0] == "push_front":
        dq = dq.push_front(cmd[1])
        print("ok")
    elif cmd[0] == "push_back":
        dq = dq.push_back(cmd[1])
        print("ok")
    elif cmd[0] == "pop_front":
        value, dq = dq.pop_front()
        print(value if value is not None else "error")
    elif cmd[0] == "pop_back":
        value, dq = dq.pop_back()
        print(value if value is not None else "error")
    elif cmd[0] == "front":
        print(dq.front() if dq.front() is not None else "error")
    elif cmd[0] == "back":
        print(dq.back() if dq.back() is not None else "error")
    elif cmd[0] == "size":
        print(dq.size())
    elif cmd[0] == "clear":
        dq = dq.clear()
        print("ok")
    elif cmd[0] == "exit":
        print("bye")
        break