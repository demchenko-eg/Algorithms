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

    def Print(self) -> None:
        """Вивести елементи Зв’язного Списку"""
        curr = self.head
        out = []
        while curr:
            out.append(str(curr.data))
            curr = curr.next
        print(" ".join(out))

    def PrintReverse(self) -> None:
        """Вивести елементи Зв’язного Списку в зворотному порядку"""
        def _rev(node: "Node | None") -> None:
            if node is None:
                return
            _rev(node.next)
            out.append(str(node.data))
        out = []
        _rev(self.head)
        print(" ".join(out))

if __name__ == '__main__':
    n = int(input().strip())
    numbers = list(map(int, input().split()))
    lst = List()
    for num in numbers:
        lst.addToTail(num)
    lst.Print()
    lst.PrintReverse()