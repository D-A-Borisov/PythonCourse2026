class Node:
    """
    Вспомогательный класс для узлов списка
    """
    def __init__(self, data):
        self.data = data  # храним информацию
        self.nref = None  # ссылка на следующий узел
        self.pref = None  # Ссылка на предыдущий узел


class Queue:
    """
    Основной класс для очереди
    """
    def __init__(self):
        self.start = None  # ссылка на начало очереди
        self.end = None    # ссылка на конец очереди
        self.length = 0    # длина очереди для удобства

    def pop(self):
        """
        возвращаем элемент val из начала списка с удалением из списка
        """
        if self.start is None:
            raise IndexError("Очередь пуста")

        val = self.start.data

        if self.start.nref:
            self.start.nref.pref = None
        self.start = self.start.nref

        if self.start is None:  # Если очередь стала пустой
            self.end = None

        self.length -= 1
        return val

    def push(self, val):
        """
        добавление элемента val в конец списка
        """
        new_node = Node(val)

        if self.end is None:  # Если очередь пуста
            self.start = new_node
            self.end = new_node
        else:
            self.end.nref = new_node
            new_node.pref = self.end
            self.end = new_node

        self.length += 1

    def insert(self, n, val):
        """
        вставить элемент val между элементами с номерами n-1 и n
        (нумерация с 0)
        """
        if n < 0 or n > self.length:
            raise IndexError("Неверная позиция для вставки")

        if n == 0:  # Вставка в начало
            new_node = Node(val)
            new_node.nref = self.start
            if self.start:
                self.start.pref = new_node
            self.start = new_node
            if self.end is None:
                self.end = new_node

        elif n == self.length:  # Вставка в конец
            self.push(val)
            return  # push уже увеличивает length

        else:  # Вставка в середину
            new_node = Node(val)
            current = self.start

            # Находим элемент на позиции n
            for _ in range(n):
                current = current.nref

            # Вставляем перед current
            new_node.pref = current.pref
            new_node.nref = current
            current.pref.nref = new_node
            current.pref = new_node

        self.length += 1

    def print(self):
        """
        вывод на печать содержимого очереди
        """
        if self.start is None:
            print("Очередь пуста")
            return

        current = self.start
        result = []
        while current:
            result.append(str(current.data))
            current = current.nref

        print(" <-> ".join(result) + f" (длина: {self.length})")


if __name__ == "__main__":
    print("\nТестирование очереди:")
    queue = Queue()
    queue.push(1)
    queue.push(2)
    queue.push(3)
    queue.print()  # 1 <-> 2 <-> 3 (длина: 3)

    queue.insert(1, 99)
    queue.print()  # 1 <-> 99 <-> 2 <-> 3 (длина: 4)

    print(f"Извлечен: {queue.pop()}")  # 1
    queue.print()  # 99 <-> 2 <-> 3 (длина: 3)
