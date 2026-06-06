import shutil
import os


def copy_file(source, destination):
    """Копирование файла"""
    try:
        if not os.path.exists(source):
            print(f"️ Исходный файл {source} не найден.")
            return False

        shutil.copy2(source, destination)  # copy2 сохраняет метаданные
        print(f" Файл '{source}' скопирован в '{destination}'")
        print(f"   Размер файла: {os.path.getsize(destination)} байт")
        return True
    except Exception as e:
        print(f" Ошибка при копировании: {e}")
        return False


def delete_file(filename):
    """Удаление файла"""
    try:
        if not os.path.exists(filename):
            print(f" Файл {filename} не найден.")
            return False

        os.remove(filename)
        print(f" Файл '{filename}' успешно удалён.")
        return True
    except Exception as e:
        print(f" Ошибка при удалении: {e}")
        return False


if __name__ == "__main__":
    print("=== Копирование и удаление файлов ===\n")

    # Создаём тестовый файл
    with open('test_source.txt', 'w', encoding='utf-8') as f:
        f.write("Это тестовый файл для демонстрации копирования.\nДата создания: 2026")

    # Копируем
    copy_file('test_source.txt', 'test_destination.txt')

    # Удаляем оба файла
    delete_file('test_destination.txt')
    delete_file('test_source.txt')