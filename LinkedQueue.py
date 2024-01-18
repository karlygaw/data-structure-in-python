class LinkedQueue:
    """
    Реализация очереди через односвязный список
    """

    class _Node:
        """
        Непубличный класс, необходимы йдля хранения каждого узла
        """
        def __init__(self, data, next):
            self._data = data
            self._next = next

        def __repr__(self):
            return str(self._data)

    def __init__(self):
        """
        Конструктор пустой очереди
        """
        self._head = None
        self._tail = None
        self._size = 0

    def __len__(self):
        """
        Возвращаем длину очереди
        """
        return self._size

    def is_empty(self):
        """
        Проверка на пустоту
        """
        return self._size == 0

    def first(self):
        """
         Просмотр первого элемента
        """
        if self.is_empty():
            raise Empty("Очередь пуста")

        return self._head._data

    def dequeue(self):
        """
        Удаляем первый элемент в очереди
        """
        if self.is_empty():
            raise Empty("Очередь пуста")

        data = self._head._data
        self._head = self._head._next

        self._size -= 1

        if self.is_empty():
            self._tail = None
        return data

    def enqueue(self, elem):
        """
        Добавление в конец очереди
        """
        newest = self._Node(elem, None)
        if self.is_empty():
            self._head = newest
        else:
            self._tail._next = newest
        self._tail = newest
        self._size += 1

    def reverse_first_k(self, k):
        """
        Обращение первых K элементов в очереди
        """
        if k <= 0 or k > len(self):
            return

        prev = None
        current = self._head
        for _ in range(k):
            next_node = current._next
            current._next = prev
            prev = current
            current = next_node

        self._head = prev

    def __repr__(self):
        ret_str = ""
        ret_str = ret_str + '['
        trav = self._head
        while trav is not None:
            ret_str = ret_str + str(trav._data)
            if trav._next is not None:
                ret_str = ret_str + ', '
            trav = trav._next

        ret_str = ret_str + ']'
        return str(ret_str)

queue = LinkedQueue()

# for i in range(10):
#     queue.enqueue(i)

# print(queue.first())

# queue.dequeue()
# print(queue.first())
# print(queue)

for i in range(10):
    queue.enqueue(i)

print("Original Queue:", queue)
queue.reverse_first_k(5)
print("Reversed First 5 Elements:", queue)









