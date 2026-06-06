import subprocess
import sys


def add_user(username):
    """Создание нового пользователя"""
    try:
        # Проверяем, существует ли пользователь
        result = subprocess.run(['id', username], capture_output=True, text=True)
        if result.returncode == 0:
            print(f"⚠ Пользователь {username} уже существует.")
            return False

        subprocess.run(['sudo', 'useradd', '-m', username], check=True)
        print(f" Пользователь {username} успешно создан.")
        return True
    except subprocess.CalledProcessError as e:
        print(f" Ошибка при создании пользователя {username}: {e}")
        return False


def delete_user(username):
    """Удаление пользователя"""
    try:
        # Проверяем, существует ли пользователь
        result = subprocess.run(['id', username], capture_output=True, text=True)
        if result.returncode != 0:
            print(f"⚠ Пользователь {username} не существует.")
            return False

        subprocess.run(['sudo', 'userdel', '-r', username], check=True)
        print(f" Пользователь {username} успешно удалён.")
        return True
    except subprocess.CalledProcessError as e:
        print(f" Ошибка при удалении пользователя {username}: {e}")
        return False


if __name__ == "__main__":
    # Демонстрация работы
    test_user = 'test_user_17'
    print("=== Управление пользователями ===\n")
    add_user(test_user)
    delete_user(test_user)