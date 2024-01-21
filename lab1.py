import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

# Генерируем произвольную выборку
sample = np.random.normal(loc=5, scale=2, size=1000)

# Выборочное среднее значение
mean = np.mean(sample)

# Оценка дисперсии
variance = np.var(sample)

# Создание подграфиков
fig, (ax1, ax2) = plt.subplots(nrows=2, figsize=(7, 10))

# Построение гистограммы
ax1.hist(sample, bins=50, density=True, alpha=0.6, color='g')

# Построение эмпирического закона случайной величины
xmin, xmax = plt.xlim()
x = np.linspace(xmin, xmax, 100)
p = stats.norm.pdf(x, mean, variance**0.5)
ax1.plot(x, p, 'k', linewidth=2)
ax1.set_title("Гистограмма и эмпирический закон случайной величины")

# Построение статистической функции распределения.
ax2.plot(x, stats.norm.cdf(x, mean, variance**0.5), 'r', linewidth=2)
ax2.set_title("Статистическая функция распределения")

plt.tight_layout()
plt.show()
