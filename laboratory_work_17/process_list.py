import psutil
from datetime import datetime


def list_processes(limit=20):
    """Вывод списка запущенных процессов"""
    print(f"=== Список запущенных процессов ({datetime.now().strftime('%H:%M:%S')}) ===")
    print(f"{'PID':<8} {'Имя процесса':<30} {'CPU %':<8} {'Память MB':<12}")
    print("-" * 60)

    processes = []
    for proc in psutil.process_iter(['pid', 'name', 'cpu_percent', 'memory_info']):
        try:
            proc_info = proc.info
            mem_mb = proc_info['memory_info'].rss / 1024 / 1024 if proc_info['memory_info'] else 0
            processes.append({
                'pid': proc_info['pid'],
                'name': proc_info['name'][:30] if proc_info['name'] else 'N/A',
                'cpu': proc_info['cpu_percent'] or 0,
                'mem': mem_mb
            })
        except (psutil.NoSuchProcess, psutil.AccessDenied):
            continue

    # Сортируем по использованию CPU
    processes.sort(key=lambda x: x['cpu'], reverse=True)

    for i, proc in enumerate(processes[:limit]):
        print(f"{proc['pid']:<8} {proc['name']:<30} {proc['cpu']:<8.1f} {proc['mem']:<12.2f}")

    print(f"\n📊 Всего процессов: {len(processes)} (показано {min(limit, len(processes))})")


def find_process_by_name(name_pattern):
    """Поиск процесса по имени"""
    print(f"\n🔍 Поиск процессов, содержащих '{name_pattern}':")
    found = False
    for proc in psutil.process_iter(['pid', 'name']):
        try:
            if name_pattern.lower() in proc.info['name'].lower():
                print(f"   PID: {proc.info['pid']}, Имя: {proc.info['name']}")
                found = True
        except (psutil.NoSuchProcess, psutil.AccessDenied):
            continue

    if not found:
        print(f"   Процессы с именем '{name_pattern}' не найдены.")


if __name__ == "__main__":
    list_processes(limit=15)
    find_process_by_name("python")