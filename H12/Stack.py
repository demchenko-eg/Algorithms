class Node:
    """ Допоміжний клас, що реалізує вузол стеку """
    def __init__(self, item):
    # """ Конструктор
    # :param item: навантаження вузла
    # """
        self.item = item # створюємо поле для зберігання навантаження
        self.next = None # посилання на наступний вузол стеку


class Stack:
    """ Клас, що реалізує стек елементів
    як рекурсивну структуру """
    def __init__(self):
    # """ Конструктор ""
        self.top_node = None # посилання на верхівку стеку
    def empty(self):
        """ Перевіряє чи стек порожній
        :return: True, якщо стек порожній
        """
        return self.top_node is None
    def push(self, item):
        """ Додає елемент у стек
        :param item: елемент, що додається у стек
        """
        new_node = Node(item) # Створюємо новий вузол стеку
        new_node.next = self.top_node # Новий вузол
        # має посилатися на поточну верхівку
        self.top_node = new_node # змінюємо верхівку стека новим вузлом
    def pop(self):
        """ Забирає верхівку стека
        Сам вузол при цьому прибирається зі стеку
        :return: Навантаження верхівки стеку
        """
        if self.empty(): # Якщо стек порожній
            raise Exception("Stack: 'pop' applied to empty container")
        current_top = self.top_node # запам'ятовуємо поточну верхівку стека
        item = current_top.item # запам'ятовуємо навантаження верхівки
        self.top_node = self.top_node.next # замінюємо верхівку наступним вузлом
        del current_top # видаляємо вузол, що місить попередню верхівку