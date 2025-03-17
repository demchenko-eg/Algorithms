class Node:
    def __init__(self, item, next_=None):
        self.item = item
        self.next = next_

class Stack:
    def __init__(self):
        self.top = None
        self.cout = 0
    
    def push(self, n):
        self.top = Node(n, self.top)
        self.cout += 1
        print("ok")
    
    def pop(self):
        if self.top is not None:
            item = self.top.item
            self.top = self.top.next
            self.cout -= 1
            print(item)
        else:
            print("error")
    
    def back(self):
        if self.top is not None:
            print(self.top.item)
        else:
            print("error")
    
    def size(self):
        print(self.cout)
    
    def clear(self):
        self.top = None
        self.cout = 0
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