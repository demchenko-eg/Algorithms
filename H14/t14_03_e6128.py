class Deque:
    def __init__(self, max_size=101):
        self.arr = [0] * max_size
        self.max_size = max_size
        self.front = 0
        self.rear = 0

    def empty(self):
        return self.front == self.rear

    def push_front(self, x):
        self.front = (self.front - 1) % self.max_size
        self.arr[self.front] = x
        return "ok"

    def push_back(self, x):
        self.arr[self.rear] = x
        self.rear = (self.rear + 1) % self.max_size
        return "ok"

    def pop_front(self):
        if self.empty():
            return "error"
        x = self.arr[self.front]
        self.front = (self.front + 1) % self.max_size
        return x

    def pop_back(self):
        if self.empty():
            return "error"
        self.rear = (self.rear - 1) % self.max_size
        return self.arr[self.rear]

    def front_elem(self):
        if self.empty():
            return "error"
        return self.arr[self.front]

    def back_elem(self):
        if self.empty():
            return "error"
        return self.arr[(self.rear - 1) % self.max_size]

    def size(self):
        if self.rear >= self.front:
            return self.rear - self.front
        else:
            return self.max_size - (self.front - self.rear)

    def clear(self):
        self.front = 0
        self.rear = 0
        return "ok"

    def exit(self):
        return "bye"

if __name__ == "__main__":
    d = Deque()
    while True:
        command = input().strip()
        if not command:
            continue
        parts = command.split()
        cmd = parts[0]
        if cmd == "push_front":
            print(d.push_front(int(parts[1])))
        elif cmd == "push_back":
            print(d.push_back(int(parts[1])))
        elif cmd == "pop_front":
            print(d.pop_front())
        elif cmd == "pop_back":
            print(d.pop_back())
        elif cmd == "front":
            print(d.front_elem())
        elif cmd == "back":
            print(d.back_elem())
        elif cmd == "size":
            print(d.size())
        elif cmd == "clear":
            print(d.clear())
        elif cmd == "exit":
            print(d.exit())
            break