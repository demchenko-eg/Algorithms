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

    def ReorderList(self) -> None:
        """Перегрупувати елементи списку як наведено вище"""
        if self.head is None or self.head.next is None:
            return
        slow = self.head
        fast = self.head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        second = slow.next
        slow.next = None
        prev = None
        curr = second
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        second = prev
        first = self.head
        while second:
            tmp1 = first.next
            tmp2 = second.next
            first.next = second
            second.next = tmp1
            first = tmp1
            second = tmp2
        curr = self.head
        while curr.next:
            curr = curr.next
        self.tail = curr

    def Print(self) -> None:
        """Вивести елементи Зв’язного Списку"""
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
    lst.ReorderList()
    lst.Print()