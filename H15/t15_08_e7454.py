class Node:
    def __init__(self, data: int):
        self.data: int = data
        self.next: "Node | None" = None

class List:
    def __init__(self):
        self.head: "Node | None" = None
        self.tail: "Node | None" = None

    def addToTail(self, val: int) -> None:
        """Додати число val в кінець Зв’язного Списку"""
        new_node = Node(val)
        if self.head is None:
            self.head = self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

    def hasCycle(self) -> int:
        """Повернути 1, якщо список має цикл, інакше повернути 0"""
        slow = self.head
        fast = self.head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return 1
        return 0

if __name__ == '__main__':
    p, a, b, c, m, n = map(int, input().split())
    lst = List()
    x = [0] * (n + 1)
    x[0] = p
    lst.addToTail(x[0])
    for i in range(1, n):
        x[i] = (a * x[i - 1] * x[i - 1] + b * x[i - 1] + c) % m
        lst.addToTail(x[i])
    x[n] = (a * x[n - 1] * x[n - 1] + b * x[n - 1] + c) % m
    k = x[n] % n
    if x[n] < m / 2:
        curr = lst.head
        for _ in range(k):
            curr = curr.next
        lst.tail.next = curr
    print(lst.hasCycle())