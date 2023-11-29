import ctypes

class DynamicArray:
    """
    Класс динамического массива
    """

    def __init__(self):
        self._n = 0 # кол-во элементов в массиве
        self._capacity = 1 # емкость массива
        self._A = self._make_array(self._capacity)

    def __len__(self):
        """
        Возвращаем кол-во элементов в массиве
        """
        return self._n

    def __getitem__(self, idx):
        """Возвращаем элемент массива под индексом idx"""
        if not 0 <= idx < self._n:
            raise IndexError('idx выходит за пределы массива')
        return self._A[idx]

    def append(self, obj):
        """
        Добавляем элемент в конец массива
        """
        # при повышении емкости, увеличиваем ее
        if self._n == self._capacity:
            self._resize(2 * self._capacity)
        self._A[self._n] = obj
        self._n += 1

    def insert_at(self, obj, idx):
        """
        Добавление элемента по индексу idx
        """
        if not 0 <= idx <= self._n:
            raise IndexError("idx выходит за пределы массива")

        if self._n == self._capacity:
            self._resize(2 * self._capacity)

        for i in range(self._n - 1, idx - 1, -1):
            self._A[i + 1] = self._A[i]

        self._A[idx] = obj
        self._n += 1

    def delete(self):
        """
        Удаляем элемент в конце списка
        """
        if self._n == 0:
            raise ValueError('Массив пуст')

        self._A[self._n - 1] = None
        self._n -= 1

    def _resize(self, cap): #nonpublic
        B = self._make_array(2 * cap) # новый статический массив с большей емкостью
        for i in range(self._n):
            B[i] = self._A[i]

        self._A = B
        self._capacity = cap

    def _make_array(self, cap): # nonpublic
        """
        Возвращаем массив с емкость сар
        """
        return (cap * ctypes.py_object)()

    def find_maximum(self):
        """
        Находим максимальный элемент в массиве
        """
        if self._n == 0:
            raise ValueError('Массив пуст')

        max_num = self._A[0]
        for i in range(1, self._n):
            if self._A[i] is not None and self._A[i] > max_num:
                max_num = self._A[i]

        return max_num

    def average(self):
        """
        Находим среднее значение в массиве
        """
        if self._n == 0:
            raise ValueError('Массив пуст')

        average = self._A[0]
        for i in range(1, self._n):
                average += self._A[i]

        return average/self._n

    def common_elements(self, arr2):
        """
        Находим common elements
        """
        set_arr1 = set(self._A[x] for x in range(self._n) if self._A[x] is not None)
        set_arr2 = set(x for x in arr2 if x is not None)

        common_elements = list(set_arr1.intersection(set_arr2))
        return common_elements

    def sort(self):
        """
        Сортируем если массив данных integer
        """
        if self._n == 0:
            raise ValueError('Массив пуст')

        if not all(isinstance(self._A[x], int) for x in range(self._n) if self._A[x] is not None):
            raise TypeError('Массив должен содержать только целые числа')

        for i in range(self._n - 1):
            for j in range(0, self._n - i - 1):
                if self._A[j] > self._A[j + 1]:
                    self._A[j], self._A[j + 1] = self._A[j + 1], self._A[j]

    def smallest_largest(self):
        """
        10.	Find the smallest and largest strings in an array of strings.
        """
        if self._n == 0:
            raise ValueError('Массив пуст')

        if not all(isinstance(self._A[x], str) for x in range(self._n) if self._A[x] is not None):
            raise TypeError('Массив должен содержать только строки')

        smallest_str = largest_str = self._A[0]
        for i in range(1, self._n):
            if self._A[i] is not None:
                if len(self._A[i]) < len(smallest_str):
                    smallest_str = self._A[i]
                elif len(self._A[i]) > len(largest_str):
                    largest_str = self._A[i]

        return smallest_str, largest_str


# arr = DynamicArray()
# for i in range(10):
#     arr.append(i)
# arr2 = [0, 1, 2, 3, 15]

# arr.insert_at(12, 3)
# print(arr[3])
# print("Maximum number in the array:", arr.find_maximum())
# print("Average:", arr.average())
#
# print(arr.common_elements(arr2))

# for i in range(10, 0, -1):
#     arr.append(i)
#
# print("Before sorting:", )
# for i in arr:
#     print(i, end=' ')
# arr.sort()
# print()
# print("After sorting:")
# for i in arr:
#     print(i, end=' ')

arr = DynamicArray()
arr.append("apple")
arr.append("banana")
arr.append("orange")
arr.append("kiwi")

smallest, largest = arr.smallest_largest()
print("Smallest string:", smallest)
print("Largest string:", largest)

