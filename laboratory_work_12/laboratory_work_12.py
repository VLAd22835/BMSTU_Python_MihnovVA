# ЛАБОРАТОРНАЯ РАБОТА №12
# Демонстрация различных способов импорта модуля

print("=" * 60)
print("ВАРИАНТЫ ИМПОРТА МОДУЛЯ laboratory_work_12_module")
print("=" * 60)

# 1. ИМПОРТ ВСЕГО МОДУЛЯ
print("\n1. Импорт всего модуля:")
print("-" * 40)
import laboratory_work_12_module as module

print(f"add(5, 10) = {module.add(5, 10)}")
print(f"subtract(5, 10) = {module.subtract(5, 10)}")
print(f"multiply(5, 10) = {module.multiply(5, 10)}")
print(f"divide(5, 10) = {module.divide(5, 10)}")
print(f"PI = {module.PI}")

# 2. ИМПОРТ КОНКРЕТНЫХ ЭЛЕМЕНТОВ
print("\n2. Импорт конкретных элементов:")
print("-" * 40)
from laboratory_work_12_module import add, multiply, PI

print(f"add(5, 10) = {add(5, 10)}")
print(f"multiply(5, 10) = {multiply(5, 10)}")
print(f"PI = {PI}")

# 3. ИМПОРТ С ПЕРЕИМЕНОВАНИЕМ
print("\n3. Импорт с переименованием:")
print("-" * 40)
from laboratory_work_12_module import add as addition, multiply as multiplication, PI as pi_value

print(f"addition(5, 10) = {addition(5, 10)}")
print(f"multiplication(5, 10) = {multiplication(5, 10)}")
print(f"pi_value = {pi_value}")

# 4. ИМПОРТ ВСЕХ ЭЛЕМЕНТОВ (через __all__)
print("\n4. Импорт всех элементов (используется __all__):")
print("-" * 40)
from laboratory_work_12_module import *

print(f"add(5, 10) = {add(5, 10)}")
print(f"subtract(5, 10) = {subtract(5, 10)}")
print(f"multiply(5, 10) = {multiply(5, 10)}")
print(f"divide(5, 10) = {divide(5, 10)}")
print(f"PI = {PI}")

# Проверяем, что приватные функции не импортировались
try:
    print(_power(2, 3))
except NameError:
    print("\nПримечание: _power и _divide не импортированы, т.к. их нет в __all__")

print("\n" + "=" * 60)
print("Демонстрация специальной переменной __name__:")
print("=" * 60)
print(f"__name__ в главной программе: {__name__}")
print("(в модуле __name__ будет равен 'laboratory_work_12_module' при импорте)")