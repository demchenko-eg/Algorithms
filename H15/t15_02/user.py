class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

head = None
tail = None
cur = None

def init():
    global head, tail, cur
    head = None
    tail = None
    cur = None

def empty():
    return head is None

def reset():
    global cur
    cur = head

def next():
    global cur
    if cur is None or cur.next is None:
        raise StopIteration()
    cur = cur.next

def current():
    if cur is None:
        raise Exception()
    return cur.value

def insert_after(item):
    global head, tail, cur
    new_node = Node(item)
    if empty():
        head = tail = cur = new_node
    else:
        new_node.next = cur.next
        cur.next = new_node
        if cur == tail:
            tail = new_node

def insert_before(item):
    global head, tail, cur
    new_node = Node(item)
    if empty():
        head = tail = cur = new_node
    elif cur == head:
        new_node.next = head
        head = new_node
    else:
        prev = head
        while prev is not None and prev.next != cur:
            prev = prev.next
        if prev is None:
            raise Exception()
        prev.next = new_node
        new_node.next = cur

def delete():
    global head, tail, cur
    if empty() or cur is None:
        return
    if cur == head:
        head = head.next
        cur = head
        if head is None:
            tail = None
    else:
        prev = head
        while prev is not None and prev.next != cur:
            prev = prev.next
        if prev is None:
            return
        prev.next = cur.next
        if cur == tail:
            tail = prev
        cur = prev.next if prev.next is not None else prev

def damp():
    result = []
    node = head
    while node is not None:
        result.append(node.value)
        node = node.next
    return result