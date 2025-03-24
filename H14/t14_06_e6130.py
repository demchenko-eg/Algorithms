class Node:
    def __init__(self, value):
        self.value = value
        self.prev = None
        self.next = None

class Deque:
    def __init__(self):
        self.head = None
        self.tail = None
        self.count = 0
    def push_front(self, item):
        new_node = Node(item)
        if self.head is None:
            self.head = self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        self.count += 1
        return "ok"
    def push_back(self, item):
        new_node = Node(item)
        if self.tail is None:
            self.head = self.tail = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node
        self.count += 1
        return "ok"
    def pop_front(self):
        if self.head is None:
            return "error"
        value = self.head.value
        self.head = self.head.next
        if self.head is not None:
            self.head.prev = None
        else:
            self.tail = None
        self.count -= 1
        return value
    def pop_back(self):
        if self.tail is None:
            return "error"
        value = self.tail.value
        self.tail = self.tail.prev
        if self.tail is not None:
            self.tail.next = None
        else:
            self.head = None
        self.count -= 1
        return value
    def front(self):
        if self.head is None:
            return "error"
        return self.head.value
    def back(self):
        if self.tail is None:
            return "error"
        return self.tail.value
    def size(self):
        return self.count
    def clear(self):
        self.head = None
        self.tail = None
        self.count = 0
        return "ok"

d = Deque()
while True:
    cmd = input().split()
    if cmd[0] == "push_front":
        print(d.push_front(int(cmd[1])))
    elif cmd[0] == "push_back":
        print(d.push_back(int(cmd[1])))
    elif cmd[0] == "pop_front":
        print(d.pop_front())
    elif cmd[0] == "pop_back":
        print(d.pop_back())
    elif cmd[0] == "front":
        print(d.front())
    elif cmd[0] == "back":
        print(d.back())
    elif cmd[0] == "size":
        print(d.size())
    elif cmd[0] == "clear":
        print(d.clear())
    elif cmd[0] == "exit":
        print("bye")
        break