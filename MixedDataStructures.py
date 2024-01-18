class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()

    def peek(self):
        if not self.is_empty():
            return self.items[-1]

    def size(self):
        return len(self.items)


class Queue:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if not self.is_empty():
            return self.items.pop(0)

    def size(self):
        return len(self.items)


def print_alternating_order(elements):
    stack = Stack()
    queue = Queue()

    # Поместить элементы в стек и поставить их в очередь
    for element in elements:
        stack.push(element)
        queue.enqueue(element)

    # Выводить элементов в чередующемся порядке
    while not stack.is_empty() and not queue.is_empty():
        print(stack.pop(), end=' ')
        print(queue.dequeue(), end=' ')

    # Выводить все оставшиеся элементы в стеке
    while not stack.is_empty():
        print(stack.pop(), end=' ')

    # Выводить все оставшиеся элементы в стеке
    while not queue.is_empty():
        print(queue.dequeue(), end=' ')


# Пример использования
elements_to_print = [1, 2, 3, 4, 5]
print_alternating_order(elements_to_print)
