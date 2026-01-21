class Node:
    """
    Вспомогательный класс для узлов списка
    """
    def __init__(self, data):
        self.data = data  # храним информацию
        self.pref = None  # ссылка на предыдущий узел


class Stack:
    """
    Основной класс для стека
    """
    def __init__(self):
        self.end = None  # ссылка на конец стека (верхний элемент)

    def pop(self):
        """
        возвращение последнего элемента из списка с удалением его из списка
        """
        if self.end is None:
            raise IndexError("Стек пуст")

        val = self.end.data
        self.end = self.end.pref
        return val

    def push(self, val):
        """
        добавление элемента val в конец списка
        """
        new_node = Node(val)
        new_node.pref = self.end
        self.end = new_node

    def print(self):
        """
        вывод на печать содержимого стека
        """
        if self.end is None:
            print("Стек пуст")
            return

        current = self.end
        result = []
        while current:
            result.append(str(current.data))
            current = current.pref

        print(" <- ".join(result[::-1]) + " (верх)" if result else "Стек пуст")


if __name__ == "__main__":
    print("Тестирование стека:")
    stack = Stack()
    stack.push(1)
    stack.push(2)
    stack.push(3)
    stack.print()  # 1 <- 2 <- 3 (верх)

    print(f"Извлечен: {stack.pop()}")  # 3
    stack.print()  # 1 <- 2 (верх)