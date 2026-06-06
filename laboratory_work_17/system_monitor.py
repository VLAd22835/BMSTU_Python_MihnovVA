import psutil
import time
from datetime import datetime


def monitor_resources(duration_seconds=30, interval_seconds=5):
    """
    Мониторинг системных ресурсов
    duration_seconds: общая продолжительность мониторинга
    interval_seconds: интервал между замерами
    """
    start_time = time.time()
    measurement_count = 0

    print(f"=== Мониторинг системных ресурсов ===")
    print(f"Начало: {datetime.now().strftime('%H:%M:%S')}")
    print(f"Продолжительность: {duration_seconds} сек, интервал: {interval_seconds} сек\n")

    while time.time() - start_time < duration_seconds:
        measurement_count += 1
        print(f" Замер #{measurement_count} - {datetime.now().strftime('%H:%M:%S')}")
        print(f"   ├─ CPU загрузка: {psutil.cpu_percent(interval=1)}%")
        print(f"   ├─ Оперативная память: {psutil.virtual_memory().percent}% (использовано)")
        print(f"   ├─ Диск (/) заполнен на: {psutil.disk_usage('/').percent}%")
        print(f"   └─ Время работы системы: {psutil.boot_time()}")
        print("-" * 40)

        if time.time() - start_time < duration_seconds - interval_seconds:
            time.sleep(interval_seconds)

    print(f"\n Мониторинг завершён. Выполнено замеров: {measurement_count}")


def quick_monitor():
    """Быстрый однократный замер"""
    print("=== Быстрый замер ресурсов ===")
    print(f"CPU: {psutil.cpu_percent(interval=1)}%")
    print(f"RAM: {psutil.virtual_memory().percent}%")
    print(f"DISK: {psutil.disk_usage('/').percent}%")


if __name__ == "__main__":
    # Выбор режима
    # quick_monitor()  # разовый замер
    monitor_resources(duration_seconds=15, interval_seconds=5)  # 15 секунд с интервалом 5 сек