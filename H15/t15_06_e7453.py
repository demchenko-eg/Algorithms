class Node:
    def __init__(self, data: int):
        self.data: int = data
        self.next: "Node | None" = None

class List:
    def __init__(self):
        self.head: "Node | None" = None
        self.tail: "Node | None" = None

    def addToTail(self, val: int) -> None:
        """Додати число val в кінець зв’язного списку."""
        new_node = Node(val)
        if self.head is None:
            self.head = self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

    def RotateRight(self, k: int) -> None:
        """Обертає список праворуч на k позицій."""
        if self.head is None or self.head.next is None:
            return
        n = 1
        curr = self.head
        while curr.next:
            curr = curr.next
            n += 1
        curr.next = self.head
        k %= n
        if k == 0:
            curr.next = None
            return
        steps_to_new_tail = n - k - 1
        new_tail = self.head
        for _ in range(steps_to_new_tail):
            new_tail = new_tail.next
        new_head = new_tail.next
        new_tail.next = None
        self.head = new_head
        self.tail = new_tail

    def Print(self) -> None:
        """Вивести елементи зв’язного списку у прямому порядку."""
        curr = self.head
        out = []
        while curr:
            out.append(str(curr.data))
            curr = curr.next
        print(" ".join(out))

if __name__ == '__main__':
    n = int(input().strip())
    numbers = list(map(int, input().split()))
    lst = List()
    for num in numbers:
        lst.addToTail(num)
    while True:
        try:
            k = int(input().strip())
        except EOFError:
            break
        except Exception:
            break
        lst.RotateRight(k)
        lst.Print()