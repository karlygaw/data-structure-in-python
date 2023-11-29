class DoublyLinkedLists:

    class _Node():
        """
        Непубличный класс для хранения каждого конкретного узла
        """

        def __init__(self, data, prev, next):
            self._data = data
            self._prev = prev
            self._next = next
            self._trav_iter = None

    def  __init__(self):
        self._head = None
        self._tail = None
        self._size = 0


    def __len__(self):
        """
        returning the len of the list
        """
        return self._size

    def is_empty(self):
        """
        Проверка на пустоту
        """
        return self._size == 0

    def add_last(self, elem):
        """
        adding to the end of the list, O(1)
        """
        if self.is_empty():
            self._head = self._tail = self._Node(elem, None, None)
        else:
            self._tail._next = self._Node(elem, self._tail, None)
            self._tail = self._tail._next
        self._size += 1

    def add_first(self, elem):
        """
        Добавление в начало списка
        """
        if self.is_empty():
            self._head = self._tail = self._Node(elem, None, None)
        else:
            self._head._prev = self._Node(elem, None, self._head)
            self._head = self._head._prev

        self._size += 1

    def add_at(self, elem, idx):
        """
        Добавление элемента в список по индексу, O(n)
        """
        if idx < 0:
            raise IndexError()

        if idx == 0:
            self.add_first(elem)
            return

        if idx == self._size:
            self.add_last(elem)
            return

        temp = self._head
        for i in range(0, idx - 1):
            temp = temp._next

        new_node = self._Node(elem, temp, temp._next)
        temp._next._prev = new_node
        temp._next = new_node

        self._size += 1

    def peek_first(self):
        """
        Просмотр значения в голове связного списка. O(1)
        """
        if self.is_empty():
            raise Empty('Список пуст')
        return self._head._data

    def peek_last(self):
        """
        Просмотр значения в хвосте связного списка. O(1)
        """
        if self.is_empty():
            raise Empty('Список пуст')
        return self._tail._data

    def remove_first(self):
        """
        Удаление из головы списка, О(1)
        """
        if self.is_empty():
            raise Empty('Список пуст')

        data = self._head._data
        self._head = self._head._next
        self._size -= 1

        if self.is_empty():
            self._tail = None
        else:
            self._head._prev = None

        return data

    def remove_last(self):
        """
        Удаление из хвоста списка, О(1)
        """
        if self.is_empty():
            raise  Empty('Список пуст')

        data = self._tail._data
        self._tail = self._tail._prev
        self._size -= 1

        if self.is_empty():
            self._head = None
        else:
            self._tail._next = None

        return data

    def __remove__(self, node):
        """
        Удаление определенного узла, О(1)
        """
        if node._prev == None:
            return self.remove_first()
        if node._next == None:
            return self.remove_last()

        #меняем указатели
        node._next._prev = node._prev
        node._prev._next = node._next

        data = node._data

        node._data = None
        node.prev = None
        node.next = None

        self._size -= 1
        return data




    def remove_at(self, idx):
        """
        Удаление из списка по индексу, О(n)
        """
        if not 0 <= idx < self._size:
            raise ValueError()

        if idx < self._size / 2:
            i = 0
            trav = self._head
            while i != idx:
                i += 1
                trav = trav._next

        else:
            i = self._size - 1
            trav = self._tail
            while i != idx:
                i -= 1
                trav = trav._prev

        return self.__remove__(trav)

    def remove(self, obj):
        """
        Удаление определенного значения, O(n)
        """
        trav = self._head
        if obj == None:
            trav = self._head
            while trav is not None:
                if trav._data is None:
                    self.__remove__(trav)
                    return True
                trav = trav._next
        else:
            trav = self._head

            while trav is not None:
                if obj == trav._data:
                    self.__remove__(trav)
                    return True
                trav = trav._next

        return False

    def index_of(self, obj):
        """
        Поиск индекса определенного значения, O(N)
        """
        idx = 0

        trav = self._head
        if obj is None:
            while trav is not None:
                if trav._data is None:
                    return idx

                idx += 1
                trav = trav._next
        else:
            while trav is not None:
                if obj == trav._data:
                    return idx
                idx += 1
                trav = trav._next

        return -1

    def contains(self, obj):
        """
        Проверка наличия обьекта, O(n)
        """
        return self.index_of(obj) != -1

    def reverse(self):
        """
        Перевернуть список
        """
        current = self._head
        while current is not None:
            # Меняем местами указатели предыдущего и следующего узла текущего узла
            current._prev, current._next = current._next, current._prev
            # Переходим к следующему узлу
            current = current._prev

        # Поменять местами указатели головы и хвоста после перебора
        self._head, self._tail = self._tail, self._head

    def middle_element(self):
        """
        Find the middle element(s) of the doubly linked list.
        """
        if self.is_empty():
            raise Empty('Список пуст')

        slow = self._head
        fast = self._head

        while fast is not None and fast._next is not None:
            slow = slow._next
            fast = fast._next._next

        # Если в списке нечетное кол-во элементов, вернуть один средний элемент.
        if self._size % 2 == 1:
            return slow._data
        # Если в списке четное кол-во элементов, вернуть два средних элемента.
        else:
            return slow._prev._data, slow._data

    def remove_duplicates(self):
        """
        Удаление дубликатов
        """
        if self.is_empty():
             raise Empty('Список пуст')

        seen_elements = set()
        current = self._head

        while current is not None:
            data = current._data

            # Check if the element is already seen
            if data in seen_elements:
                # Remove the duplicate element
                self.__remove__(current)
            else:
                # Add the element to the set of seen elements
                seen_elements.add(data)
                current = current._next

    def detect_loop(head):
        """
        10.	Write a function to detect a loop in a linked list.
        """
        slow_pointer = head
        fast_pointer = head

        while fast_pointer is not None and fast_pointer._next is not None:
            slow_pointer = slow_pointer.next
            fast_pointer = fast_pointer.next.next

            if slow_pointer == fast_pointer:
                return True

        return False

    def __iter__(self):
        """
        Вызывается при создании итерации
        """
        self._trav_iter = self._head
        return self

    def __next__(self):
        """
        Необходима для перехода к следующему элементу
        """
        # остановку итерации при достижении конца нашего списка
        if self._trav_iter is None:
            raise StopIteration

        # хранение данных _trav_iter.data
        data = self._trav_iter._data
        self._trav_iter = self._trav_iter._next

        return data


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

dll = DoublyLinkedLists()
dll.add_first(12)
dll.add_last(120)
print(dll._head._data)
print(dll)

for i in range(10):
    dll.add_last(i)

dll.add_last(1)
dll.add_last(5)
print(dll)
dll.remove_duplicates()
print(dll)
dll.add_last(5)
print(dll)

dll.add_at(30, 3)
print(dll)

dll.remove(9)
print(dll)
print(dll.index_of(3))
print(dll.index_of(9))


dll.reverse()
print(dll)

print("Middle element: ",dll.middle_element())




