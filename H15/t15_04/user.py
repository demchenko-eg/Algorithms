class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None

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

def set_first():
    global cur
    cur = head

def set_last():
    global cur
    cur = tail

def next():
    global cur
    if cur is None or cur.next is None:
        raise StopIteration()
    cur = cur.next

def prev():
    global cur
    if cur is None or cur.prev is None:
        raise StopIteration()
    cur = cur.prev

def current():
    return cur.value

def insert_after(item):
    global head, tail, cur
    new_node = Node(item)
    if empty():
        head = tail = cur = new_node
    else:
        new_node.prev = cur
        new_node.next = cur.next
        if cur.next is not None:
            cur.next.prev = new_node
        else:
            tail = new_node
        cur.next = new_node

def insert_before(item):
    global head, tail, cur
    new_node = Node(item)
    if empty():
        head = tail = cur = new_node
    else:
        new_node.next = cur
        new_node.prev = cur.prev
        if cur.prev is not None:
            cur.prev.next = new_node
        else:
            head = new_node
        cur.prev = new_node

def delete():
    global head, tail, cur
    if empty():
        return
    if cur.next is not None:
        new_current = cur.next
    else:
        new_current = cur.prev
    if cur.prev is not None:
        cur.prev.next = cur.next
    else:
        head = cur.next
    if cur.next is not None:
        cur.next.prev = cur.prev
    else:
        tail = cur.prev
    cur = new_current

def damp():
    result = []
    node = head
    while node is not None:
        result.append(node.value)
        node = node.next
    return result

def len():
    count = 0
    node = head
    while node is not None:
        count += 1
        node = node.next
    return count

def swap_prev():
    global head, tail, cur
    if cur is None or cur.prev is None:
        raise Exception()
    prev_node = cur.prev
    A = prev_node.prev
    B = cur.next
    cur.prev = A
    cur.next = prev_node
    prev_node.prev = cur
    prev_node.next = B
    if A:
        A.next = cur
    else:
        head = cur
    if B:
        B.prev = prev_node
    else:
        tail = prev_node

def swap_next():
    global head, tail, cur
    if cur is None or cur.next is None:
        raise Exception()
    next_node = cur.next
    A = cur.prev
    B = next_node.next
    if A:
        A.next = next_node
    else:
        head = next_node
    next_node.prev = A
    next_node.next = cur
    cur.prev = next_node
    cur.next = B
    if B:
        B.prev = cur
    else:
        tail = cur