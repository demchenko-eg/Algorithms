class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None

class Deque:
    def __init__(self):
        self.head = None
        self.tail = None
        self._size = 0

    def push_front(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        self._size += 1
        return "ok"

    def _push_back_r(self, node, new_node):
        if node.next is None:
            node.next = new_node
            new_node.prev = node
            return new_node
        return self._push_back_r(node.next, new_node)

    def push_back(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = self.tail = new_node
        else:
            self.tail = self._push_back_r(self.tail, new_node)
        self._size += 1
        return "ok"

    def pop_front(self):
        if self.head is None:
            return "error"
        value = self.head.value
        self.head = self.head.next
        if self.head is None:
            self.tail = None
        else:
            self.head.prev = None
        self._size -= 1
        return value

    def _pop_back_r(self, node):
        if node.next is None:
            value = node.value
            if node.prev is None:
                return None, value
            node.prev.next = None
            return node.prev, value
        new_tail, value = self._pop_back_r(node.next)
        return new_tail, value

    def pop_back(self):
        if self.head is None:
            return "error"
        self.tail, value = self._pop_back_r(self.tail)
        if self.tail is None:
            self.head = None
        self._size -= 1
        return value

    def front(self):
        if self.head is None:
            return "error"
        return self.head.value

    def _back_r(self, node):
        if node.next is None:
            return node.value
        return self._back_r(node.next)

    def back(self):
        if self.tail is None:
            return "error"
        return self.tail.value

    def size(self):
        return self._size

    def clear(self):
        self.head = self.tail = None
        self._size = 0
        return "ok"

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
        print(dq.push_front(cmd[1]))
    elif cmd[0] == "push_back":
        print(dq.push_back(cmd[1]))
    elif cmd[0] == "pop_front":
        print(dq.pop_front())
    elif cmd[0] == "pop_back":
        print(dq.pop_back())
    elif cmd[0] == "front":
        print(dq.front())
    elif cmd[0] == "back":
        print(dq.back())
    elif cmd[0] == "size":
        print(dq.size())
    elif cmd[0] == "clear":
        print(dq.clear())
    elif cmd[0] == "exit":
        print("bye")
        break