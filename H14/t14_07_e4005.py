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
    def empty(self):
        return self.count == 0
    def push_front(self, item):
        new_node = Node(item)
        if self.head is None:
            self.head = self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        self.count += 1
    def push_back(self, item):
        new_node = Node(item)
        if self.tail is None:
            self.head = self.tail = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node
        self.count += 1
    def pop_front(self):
        if self.head is None:
            return None
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
            return None
        value = self.tail.value
        self.tail = self.tail.prev
        if self.tail is not None:
            self.tail.next = None
        else:
            self.head = None
        self.count -= 1
        return value

n = int(input())
first_cards = list(map(int, input().split()))
second_cards = list(map(int, input().split()))
d1 = Deque()
d2 = Deque()
for card in first_cards:
    d1.push_back(card)
for card in second_cards:
    d2.push_back(card)
moves = 0
max_moves = 200000
while not d1.empty() and not d2.empty() and moves < max_moves:
    moves += 1
    card1 = d1.pop_front()
    card2 = d2.pop_front()
    if card1 == 0 and card2 == n - 1:
        d1.push_back(card1)
        d1.push_back(card2)
    elif card1 == n - 1 and card2 == 0:
        d2.push_back(card1)
        d2.push_back(card2)
    elif card1 > card2:
        d1.push_back(card1)
        d1.push_back(card2)
    else:
        d2.push_back(card1)
        d2.push_back(card2)
if moves >= max_moves:
    print("draw")
else:
    if d1.empty():
        print("second", moves)
    else:
        print("first", moves)