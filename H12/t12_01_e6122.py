class Stack:
    def __init__(self, maxsize=100):
        self.stack = [None] * maxsize
        self.maxsize = maxsize
        self.top = -1
    
    def push(self, n):
        if self.top < self.maxsize - 1:
            self.top += 1
            self.stack[self.top] = n
            print("ok")
    
    def pop(self):
        if self.top >= 0:
            print(self.stack[self.top])
            self.top -= 1
    
    def back(self):
        if self.top >= 0:
            print(self.stack[self.top])
    
    def size(self):
        print(self.top + 1)
    
    def clear(self):
        self.top = -1
        print("ok")
    
    def exit(self):
        print("bye")
        quit()

if __name__ == "__main__":
    stack = Stack()
    while True:
        command = input().split()
        if command[0] == "push":
            stack.push(int(command[1]))
        elif command[0] == "pop":
            stack.pop()
        elif command[0] == "back":
            stack.back()
        elif command[0] == "size":
            stack.size()
        elif command[0] == "clear":
            stack.clear()
        elif command[0] == "exit":
            stack.exit()
