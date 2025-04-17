heap = []
pos = {}

def sift_up(i):
    while i > 0:
        p = (i - 1) // 2
        if heap[p][1] < heap[i][1]:
            heap[p], heap[i] = heap[i], heap[p]
            pos[heap[p][0]] = p
            pos[heap[i][0]] = i
            i = p
        else:
            break

def sift_down(i):
    n = len(heap)
    while True:
        l = 2*i + 1
        r = 2*i + 2
        largest = i
        if l < n and heap[l][1] > heap[largest][1]:
            largest = l
        if r < n and heap[r][1] > heap[largest][1]:
            largest = r
        if largest != i:
            heap[i], heap[largest] = heap[largest], heap[i]
            pos[heap[i][0]] = i
            pos[heap[largest][0]] = largest
            i = largest
        else:
            break

def add(id, priority):
    heap.append([id, priority])
    pos[id] = len(heap) - 1
    sift_up(len(heap) - 1)

def pop_max():
    last = heap.pop()
    if not heap:
        removed = last
    else:
        removed = heap[0]
        heap[0] = last
        pos[last[0]] = 0
        sift_down(0)
    del pos[removed[0]]
    return removed

def change(id, new_priority):
    i = pos[id]
    old = heap[i][1]
    heap[i][1] = new_priority
    if new_priority > old:
        sift_up(i)
    else:
        sift_down(i)

while True:
    try:
        line = input().strip()
    except EOFError:
        break
    if not line:
        continue
    parts = line.split()
    cmd = parts[0]
    if cmd == 'ADD':
        add(parts[1], int(parts[2]))
    elif cmd == 'POP':
        id, p = pop_max()
        print(id, p)
    elif cmd == 'CHANGE':
        change(parts[1], int(parts[2]))