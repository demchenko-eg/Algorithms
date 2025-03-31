class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

head = None
cur = None

def init():
    global head, cur
    head = None
    cur = None

def empty():
    global head
    return head is None

def reset():
    global head, cur
    cur = head

def next():
    global cur
    if cur is None or cur.next is None:
        raise StopIteration()
    cur = cur.next

def current():
    global cur
    return cur.value

def insert_after(item):
    global head, cur
    new_node = Node(item)
    if head is None:
        head = new_node
        cur = new_node
    else:
        new_node.next = cur.next
        cur.next = new_node