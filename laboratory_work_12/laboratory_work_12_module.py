# Модуль с математическими функциями.

# Специальная переменная __all__ определяет, какие имена будут импортированы при импорте всех элементов
__all__ = ['add', 'subtract', 'multiply', 'divide', 'PI']

# Константы
PI = 3.14159

# Функции (4 функции + 2 приватные = 6 всего, но 4 основные)
def add(a, b):
    """Сложение двух чисел"""
    return a + b

def subtract(a, b):
    """Вычитание двух чисел"""
    return a - b

def multiply(a, b):
    """Умножение двух чисел"""
    return a * b

def divide(a, b):
    """Деление двух чисел"""
    if b == 0:
        raise ValueError("Деление на ноль невозможно.")
    return a / b

# Приватные функции (не будут импортироваться с *)
def _power(a, b):
    """Возведение в степень (приватная функция)"""
    return a ** b

def _modulus(a, b):
    """Остаток от деления (приватная функция)"""
    return a % b

# Специальная переменная __name__ для определения запуска
if __name__ == "__main__":
    print("Модуль laboratory_work_12_module запущен как программа")
    print(f"add(5, 10) = {add(5, 10)}")
    print(f"subtract(5, 10) = {subtract(5, 10)}")
    print(f"multiply(5, 10) = {multiply(5, 10)}")
    print(f"divide(5, 10) = {divide(5, 10)}")
    print(f"PI = {PI}")
else:
    print("Модуль laboratory_work_12_module импортирован")