class Node:
    def __init__(self):
        self.children = {}
        self.is_end = False

class Tree:
    def __init__(self):
        self.root = Node()
    def insert(self, number):
        node = self.root
        for digit in number:
            if node.is_end:
                return False
            if digit not in node.children:
                node.children[digit] = Node()
            node = node.children[digit]
        if node.is_end or node.children:
            return False
        node.is_end = True
        return True

def check_phone_list(phone_numbers):
    trie = Tree()
    for number in phone_numbers:
        if not trie.insert(number):
            return "NO"
    return "YES"

t = int(input().strip())
for _ in range(t):
    n = int(input().strip())
    phone_numbers = [input().strip() for _ in range(n)]
    print(check_phone_list(phone_numbers))