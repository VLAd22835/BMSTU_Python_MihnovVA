import ctypes
import sys


class MyList:
    """Собственная реализация динамического массива (списка)"""

    def __init__(self):
        self.length = 0
        self.capacity = 8
        self.array = (self.capacity * ctypes.py_object)()

    def append(self, item):
        """Добавляет элемент в конец списка"""
        if self.length == self.capacity:
            self._resize(self.capacity * 2)
        self.array[self.length] = item
        self.length += 1

    def insert(self, index, item):
        """Вставляет элемент в произвольное место списка"""
        # Обработка отрицательных индексов
        if index < 0:
            index = self.length + index + 1
        if index < 0:
            index = 0
        if index > self.length:
            index = self.length

        # Увеличиваем ёмкость при необходимости
        if self.length == self.capacity:
            self._resize(self.capacity * 2)

        # Сдвигаем элементы вправо
        for i in range(self.length, index, -1):
            self.array[i] = self.array[i - 1]

        self.array[index] = item
        self.length += 1

    def delete(self, index):
        """Удаляет элемент из произвольного места списка"""
        # Обработка отрицательных индексов
        if index < 0:
            index = self.length + index
        if index < 0 or index >= self.length:
            raise IndexError("Индекс выходит за пределы допустимого")

        # Сдвигаем элементы влево
        for i in range(index, self.length - 1):
            self.array[i] = self.array[i + 1]

        self.length -= 1
        self.array[self.length] = None  # Очищаем ссылку

        # Уменьшаем ёмкость при необходимости
        if self.length <= (self.capacity // 2 + 1) and self.capacity > 8:
            new_capacity = max(self.capacity // 2 + 1, 8)
            self._resize(new_capacity)

    def pop(self, index=-1):
        """Удаляет и возвращает элемент (по умолчанию последний)"""
        if self.length == 0:
            raise IndexError("Извлечь из пустого списка")

        # Обработка отрицательных индексов
        if index < 0:
            index = self.length + index

        if index < 0 or index >= self.length:
            raise IndexError("Индекс выходит за пределы допустимого")

        value = self.array[index]
        self.delete(index)
        return value

    def remove(self, item):
        """Удаляет первое вхождение элемента"""
        index = self.index(item)
        self.delete(index)

    def clear(self):
        """Очищает список"""
        self.length = 0
        self.capacity = 8
        self.array = (self.capacity * ctypes.py_object)()

    def index(self, item):
        """Возвращает индекс первого вхождения элемента"""
        for i in range(self.length):
            if self.array[i] == item:
                return i
        raise ValueError(f"{item} отсутствует в списке")

    def __contains__(self, item):
        """Проверяет, содержит ли список элемент (contains)"""
        for i in range(self.length):
            if self.array[i] == item:
                return True
        return False

    def __setitem__(self, index, value):
        """Устанавливает значение по индексу (setitem)"""
        if index < 0:
            index = self.length + index
        if index < 0 or index >= self.length:
            raise IndexError("Индекс выходит за пределы допустимого")
        self.array[index] = value

    def __getitem__(self, index):
        """Возвращает значение по индексу (getitem)"""
        if index < 0:
            index = self.length + index
        if index < 0 or index >= self.length:
            raise IndexError("Индекс выходит за пределы допустимого")
        return self.array[index]

    def __len__(self):
        """Возвращает длину списка"""
        return self.length

    def __str__(self):
        """Строковое представление списка"""
        items = []
        for i in range(self.length):
            items.append(repr(self.array[i]))
        return "[" + ", ".join(items) + "]"

    def __repr__(self):
        return self.__str__()

    def _resize(self, new_capacity):
        """Изменяет ёмкость массива"""
        new_array = (new_capacity * ctypes.py_object)()
        for index in range(self.length):
            new_array[index] = self.array[index]
        self.array = new_array
        self.capacity = new_capacity

    def get_capacity(self):
        """Возвращает текущую ёмкость (для отладки)"""
        return self.capacity

    def get_size_bytes(self):
        """Возвращает размер в байтах (для демонстрации)"""
        return sys.getsizeof(self.array)


# ========== ДЕМОНСТРАЦИЯ РАБОТЫ ==========
print("=" * 60)
print("ДЕМОНСТРАЦИЯ РАБОТЫ СОБСТВЕННОГО КЛАССА MyList")
print("=" * 60)

# 1. Базовые операции
print("\n1. БАЗОВЫЕ ОПЕРАЦИИ")
print("-" * 40)

my_list = MyList()
my_list.append("один")
my_list.append("два")
my_list.append("три")
print(f"Список: {my_list}")
print(f"Длина: {len(my_list)}")
print(f"Элемент по индексу 1: {my_list[1]}")

# 2. Автоматическое расширение ёмкости
print("\n2. АВТОМАТИЧЕСКОЕ РАСШИРЕНИЕ ЁМКОСТИ")
print("-" * 40)

dynamic_list = MyList()
print("Добавляем элементы в массив:")
for i in range(20):
    dynamic_list.append(i)
    print(
        f"Размер списка из {len(dynamic_list):2} элементов: ёмкость={dynamic_list.get_capacity():2}, память={dynamic_list.get_size_bytes():5} байт, значение={dynamic_list[i]}")

# 3. Автоматическое уменьшение ёмкости
print("\n3. АВТОМАТИЧЕСКОЕ УМЕНЬШЕНИЕ ЁМКОСТИ")
print("-" * 40)

print("Удаляем элементы из массива:")
for i in range(20):
    dynamic_list.pop()
    print(
        f"Размер списка из {len(dynamic_list):2} элементов: ёмкость={dynamic_list.get_capacity():2}, память={dynamic_list.get_size_bytes():5} байт")

# 4. Метод insert
print("\n4. МЕТОД insert()")
print("-" * 40)

insert_list = MyList()
for i in range(1, 4):
    insert_list.append(i)
print(f"Исходный список: {insert_list}")
insert_list.insert(1, 99)
print(f"После insert(1, 99): {insert_list}")
insert_list.insert(0, 88)
print(f"После insert(0, 88): {insert_list}")
insert_list.insert(-1, 66)
print(f"После insert(-1, 66): {insert_list}")

# 5. Метод delete
print("\n5. МЕТОД delete()")
print("-" * 40)

del_list = MyList()
for i in range(1, 6):
    del_list.append(i * 10)
print(f"Исходный список: {del_list}")
del_list.delete(2)
print(f"После delete(2): {del_list}")
del_list.delete(-1)
print(f"После delete(-1): {del_list}")

# 6. Метод pop
print("\n6. МЕТОД pop()")
print("-" * 40)

pop_list = MyList()
for i in range(1, 6):
    pop_list.append(chr(64 + i))
print(f"Исходный список: {pop_list}")
popped = pop_list.pop()
print(f"pop() вернул: {popped}, список: {pop_list}")
popped = pop_list.pop(0)
print(f"pop(0) вернул: {popped}, список: {pop_list}")

# 7. Метод remove
print("\n7. МЕТОД remove()")
print("-" * 40)

remove_list = MyList()
for item in ["яблоко", "банан", "апельсин", "банан"]:
    remove_list.append(item)
print(f"Исходный список: {remove_list}")
remove_list.remove("банан")
print(f"После remove('банан'): {remove_list}")

# 8. Метод clear
print("\n8. МЕТОД clear()")
print("-" * 40)

clear_list = MyList()
for i in range(5):
    clear_list.append(i)
print(f"До clear: {clear_list}, длина={len(clear_list)}")
clear_list.clear()
print(f"После clear: {clear_list}, длина={len(clear_list)}")

# 9. Метод index
print("\n9. МЕТОД index()")
print("-" * 40)

index_list = MyList()
for item in ["Москва", "СПб", "Казань"]:
    index_list.append(item)
print(f"Список: {index_list}")
print(f"index('Казань') = {index_list.index('Казань')}")

# 10. Оператор contains (in)
print("\n10. ОПЕРАТОР 'in'")
print("-" * 40)

contains_list = MyList()
for item in [10, 20, 30, 40, 50]:
    contains_list.append(item)
print(f"Список: {contains_list}")
print(f"30 в списке? {30 in contains_list}")
print(f"100 в списке? {100 in contains_list}")

# 11. Присваивание по индексу (setitem)
print("\n11. ПРИСВАИВАНИЕ ПО ИНДЕКСУ")
print("-" * 40)

setitem_list = MyList()
for i in range(5):
    setitem_list.append(f"элемент{i}")
print(f"Исходный список: {setitem_list}")
setitem_list[2] = "НОВЫЙ"
print(f"После setitem_list[2] = 'НОВЫЙ': {setitem_list}")
setitem_list[-1] = "ПОСЛЕДНИЙ"
print(f"После setitem_list[-1] = 'ПОСЛЕДНИЙ': {setitem_list}")

# 12. Отрицательные индексы
print("\n12. ОТРИЦАТЕЛЬНЫЕ ИНДЕКСЫ")
print("-" * 40)

neg_list = MyList()
for i in range(1, 6):
    neg_list.append(i)
print(f"Список: {neg_list}")
print(f"neg_list[-1] = {neg_list[-1]} (последний элемент)")
print(f"neg_list[-2] = {neg_list[-2]} (предпоследний)")
print(f"neg_list[-5] = {neg_list[-5]} (первый элемент)")