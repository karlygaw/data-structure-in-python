class String:
    """
    Класс String
    """

    def __init__(self):
        self._n = 0  # кол-во элементов в string
        self._string = ''  # емкость

    def __len__(self):
        """
        Возвращаем кол-во элементов в массиве
        """
        return self._n

    def __getitem__(self, idx):
        """Возвращаем элемент массива под индексом idx"""
        if isinstance(idx, int):
            if not 0 <= idx < self._n:
                raise IndexError('idx выходит за пределы массива')
            return self._string[idx]
        elif isinstance(idx, slice):
            start, stop, step = idx.indices(self._n)
            return ''.join([self._string[i] for i in range(start, stop, step)])

    def append(self, obj):
        """
        Добавляем элемент в конец string
        """
        # при повышении емкости, увеличиваем ее
        self._string += obj
        self._n += 1

    def reverse(self):
        """
        Перевернуть string
        """
        self._string = self._string[::-1]

    def is_palindrome(self):
        """
        Перевернуть string
        """
        if self._string == self._string[::-1]:
            return True
        else:
            return False

    def concatenates_two(self, string2):
        """
        7. Create a function that concatenates two strings into one.
        """
        for i in string2:
            self.append(i)

    def count_vowels(self):
        """
        8.	Implement a method to count the number of vowels in a string.
        """
        count = 0
        for i in range(self._n):
            if self._string[i].lower() in 'aeiouy':
                count += 1
            else:
                continue
        return count

    def replace_spaces(self, char):
        """
        9.	Write a program that replaces spaces in a string with a specific character.
        """
        new_str = ''
        for i in range(self._n):
            if self._string[i] ==  ' ':
                new_str += char
            else:
                new_str += self._string[i]
        self._string = new_str

str = String()
for i in 'abc ba':
    str.append(i)

print(str[:])
# str.reverse()
# print(str[:])
# print(str.is_palindrome())
# string2 = 'karlygash'
# str.concatenates_two(string2)
# print(str[:])
# print(str.count_vowels())
str.replace_spaces('!')
print(str[:])


