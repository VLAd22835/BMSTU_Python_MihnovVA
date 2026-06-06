import os
import shutil
import stat
import schedule
import time
from datetime import datetime


def create_backup(source_dir='.', backup_dir='./backups'):
    """Создание резервной копии"""
    try:
        # Создаём папку для бэкапов, если её нет
        if not os.path.exists(backup_dir):
            os.makedirs(backup_dir)
            print(f" Создана папка для бэкапов: {backup_dir}")

        # Формируем имя файла бэкапа с датой
        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
        backup_name = f"backup_{timestamp}.zip"
        backup_path = os.path.join(backup_dir, backup_name)

        # Создаём архив
        shutil.make_archive(
            backup_path.replace('.zip', ''),  # без расширения
            'zip',
            source_dir
        )

        # Получаем размер бэкапа
        size_mb = os.path.getsize(backup_path) / 1024 / 1024

        print(f" Резервная копия создана: {backup_path}")
        print(f"   Размер: {size_mb:.2f} MB")
        print(f"   Время: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        return backup_path
    except Exception as e:
        print(f" Ошибка при создании бэкапа: {e}")
        return None


def change_permissions(filepath, mode=0o644):
    """Изменение прав доступа к файлу"""
    try:
        if not os.path.exists(filepath):
            print(f"️ Файл {filepath} не найден.")
            return False

        # Изменяем права
        os.chmod(filepath, mode)

        # Получаем текущие права для отображения
        current_mode = oct(os.stat(filepath).st_mode)[-3:]

        print(f" Права доступа к '{filepath}' изменены на {oct(mode)[-3:]} ({oct(mode)})")
        print(f"   Текущие права: {current_mode}")

        # Расшифровка прав
        permissions = []
        permissions.append("чтение" if mode & stat.S_IRUSR else "")
        permissions.append("запись" if mode & stat.S_IWUSR else "")
        permissions.append("выполнение" if mode & stat.S_IXUSR else "")
        print(f"   Владелец может: {', '.join(filter(None, permissions))}")

        return True
    except Exception as e:
        print(f" Ошибка при изменении прав: {e}")
        return False


def scheduled_task():
    """Задача, выполняемая по расписанию"""
    print("\n" + "=" * 50)
    print(f" ВЫПОЛНЕНИЕ ЗАДАЧИ ПО РАСПИСАНИЮ - {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("=" * 50)
    create_backup()
    print("=" * 50 + "\n")


def run_scheduler():
    """Запуск планировщика"""
    # Настройка расписания
    schedule.every(1).minutes.do(scheduled_task)  # Каждую минуту для демонстрации
    # schedule.every().day.at("10:30").do(scheduled_task)  # Ежедневно в 10:30
    # schedule.every().hour.do(scheduled_task)  # Каждый час

    print("=== Планировщик задач запущен ===")
    print("Расписание: каждую минуту (демонстрация)")
    print("Для остановки нажмите Ctrl+C\n")

    try:
        while True:
            schedule.run_pending()
            time.sleep(1)
    except KeyboardInterrupt:
        print("\n\n️ Планировщик остановлен.")


if __name__ == "__main__":
    print("=== Резервное копирование и права доступа ===\n")

    # Создаём тестовый файл
    test_file = 'test_permissions.txt'
    with open(test_file, 'w', encoding='utf-8') as f:
        f.write("Тестовый файл для демонстрации прав доступа.\n")

    # Демонстрация изменения прав
    change_permissions(test_file, 0o644)  # rw-r--r--
    print()
    change_permissions(test_file, 0o755)  # rwxr-xr-x

    # Удаляем тестовый файл
    os.remove(test_file)

    print("\n" + "=" * 50)
    print("Для запуска планировщика раскомментируйте вызов run_scheduler()")
    print("=" * 50)

    run_scheduler()  # Раскомментируйте для запуска планировщика