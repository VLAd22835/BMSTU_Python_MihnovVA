import matplotlib.pyplot as plt
import numpy as np

# Данные
left_edge = -3.48
frequencies = [14, 22, 41, 17, 6]
n_intervals = len(frequencies)

# Ширина интервала (покрываем весь диапазон до 5.83)
width = (5.83 - left_edge) / n_intervals
edges = [left_edge + i * width for i in range(n_intervals + 1)]

# Центры интервалов для подписей
centers = [(edges[i] + edges[i+1]) / 2 for i in range(n_intervals)]

# Построение гистограммы (столбцы высотой = частота)
plt.bar(centers, frequencies, width=width * 0.9, edgecolor='black', alpha=0.7, align='center')

# Настройки
plt.xlabel('Значения')
plt.ylabel('Частота')
plt.title('Гистограмма выборки (вариант 4, 5 интервалов)')
plt.xticks(centers, [f'{edges[i]:.2f}–{edges[i+1]:.2f}' for i in range(n_intervals)], rotation=45)
plt.grid(axis='y', linestyle='--', alpha=0.7)

# Отображение частот над столбцами
for i, freq in enumerate(frequencies):
    plt.text(centers[i], freq + 0.5, str(freq), ha='center', va='bottom')

plt.tight_layout()
plt.show()