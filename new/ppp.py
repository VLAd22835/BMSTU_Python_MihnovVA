import numpy as np
import matplotlib.pyplot as plt

# Исходные данные из таблицы (столбец x(i))
data = np.array([
    -3.48, -3.45, -3.23, -2.83, -2.83, -2.64, -2.60, -2.39, -2.24, -2.19,
    -2.19, -1.99, -1.81, -1.71, -1.62, -1.52, -1.45, -1.34, -1.20, -1.14,
    -1.02, -0.95, -0.89, -0.85, -0.66, -0.64, -0.63, -0.61, -0.60, -0.55,
    -0.51, -0.47, -0.39, -0.37, -0.37, -0.25, -0.19, -0.10, -0.02, 0.01,
    0.02, 0.05, 0.11, 0.14, 0.15, 0.28, 0.33, 0.35, 0.36, 0.36,
    0.37, 0.43, 0.43, 0.48, 0.55, 0.61, 0.65, 0.84, 0.88, 0.93,
    0.97, 1.10, 1.17, 1.24, 1.26, 1.30, 1.33, 1.42, 1.47, 1.59,
    1.63, 1.63, 1.75, 1.93, 1.95, 1.98, 2.04, 2.05, 2.28, 2.36,
    2.60, 2.64, 2.69, 2.73, 2.76, 2.80, 2.85, 2.86, 2.95, 2.96,
    3.34, 3.54, 3.57, 3.86, 4.01, 4.23, 4.42, 5.50, 5.54, 5.83
])

n = len(data)

# ---- 1. Эмпирическая функция по всем данным ----
x_sorted = np.sort(data)
ecdf = np.arange(1, n + 1) / n   # F_n(x) = k/n

# ---- 2. Данные по интервалам (ваши частоты) ----
intervals = [(-3.48, -1.618), (-1.618, 0.244), (0.244, 2.106), (2.106, 3.968), (3.968, 5.83)]
freqs = [14, 22, 41, 17, 6]   # количество значений в каждом интервале
assert sum(freqs) == n, "Сумма частот не равна объёму выборки"

# Вычисляем эмпирическую функцию в правых границах интервалов
cumulative_freq = np.cumsum(freqs)
ecdf_intervals = cumulative_freq / n
interval_right_edges = [interval[1] for interval in intervals]

# Медиана по оси Y (значение 0.5)
median_y = 0.5

# ---- Визуализация ----
plt.figure(figsize=(12, 7))

# Пошаговая функция по всем точкам
plt.step(x_sorted, ecdf, where='post', label='Эмпирическая функция (по всем точкам)',
         linewidth=2, alpha=0.8, color='blue')

# Горизонтальная линия медианы по оси Y на уровне 0.5
plt.axhline(y=median_y, color='red', linestyle='-', linewidth=2.5,
            label=f'Медиана (F_n(x) = {median_y})')

# Настройка осей
plt.xlabel('x', fontsize=12, fontweight='bold')
plt.ylabel('F_n(x)', fontsize=12, fontweight='bold')
plt.title('Эмпирическая функция распределения', fontsize=14, fontweight='bold')

# Установка Y от 0.00 до 1.00 с шагом 0.1
plt.ylim(-0.02, 1.02)
plt.yticks(np.arange(0, 1.1, 0.1),
           ['0.00', '0.1', '0.2', '0.3', '0.4', '0.5', '0.6', '0.7', '0.8', '0.9', '1.00'])

# Настройка X
plt.xlim(min(data) - 0.5, max(data) + 0.5)

# Сетка
plt.grid(alpha=0.3, linestyle='--', linewidth=0.5)
plt.legend(loc='lower right', fontsize=10)

plt.tight_layout()
plt.show()

# ---- Таблица значений эмпирической функции на интервалах ----
print("=" * 85)
print("ЭМПИРИЧЕСКАЯ ФУНКЦИЯ РАСПРЕДЕЛЕНИЯ Fn(x)")
print("=" * 85)
print(f"{'Интервал':<35} {'Частота':>8} {'Накопленная частота':>20} {'Fn(x)':>12}")
print("-" * 85)

cum = 0
for i, (interv, freq) in enumerate(zip(intervals, freqs)):
    cum += freq
    fn = cum / n
    print(f"({interv[0]:7.3f}; {interv[1]:7.3f}]  {freq:8d}      {cum:18d}      {fn:11.4f}")

print("-" * 85)
print(f"\nДля x < {min(data):.2f}  -> F_n(x) = 0.0000")
print(f"Для x >= {max(data):.2f} -> F_n(x) = 1.0000")
print(f"\nМЕДИАНА ПО ОСИ Y: F_n(x) = 0.5000")