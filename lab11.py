import numpy as np
import matplotlib.pyplot as plt


# Получение данных от пользователя

def get_data():
    YES, NO, QUIET = "y", "n", "q"

    print("Сгенерировать данные для обработки?")
    choice = input("Если да введите: 'y', если нет введите 'n'" + "\n")

    if choice == YES:
        data = np.random.normal(loc=5, scale=2, size=1000)
    elif choice == NO:
        data = input("Введите числа, разделенные пробелами: ").split()
        data = list(map(float, data))
    elif choice == QUIET:
        return None
    else:
        data = get_data()

    # Сохраняем данные в файле
    with open("data.txt", "w") as file:
        for item in data:
            file.write("%s\n" % item)


data = get_data()

# Вычисление статистических характеристик
mean = np.mean(data)    # выборочное среднее
variance = np.var(data)  # оценка дисперсии

# Построение эмпирического закона распределения
plt.title('Эмпирический закон случайной величины')
values, counts = np.unique(data, return_counts=True)
plt.bar(values, counts/len(data), color='b')
plt.show()

# Построение гистограммы
plt.title('Гистограмма')
plt.hist(data, bins=len(np.unique(data)), edgecolor='black')
plt.show()

# Построение функции распределения
plt.title('Функция распределения')
cumulative_counts = np.cumsum(counts)
plt.plot(values, cumulative_counts / len(data), color='b')
plt.show()

print("Среднее значение:", mean)
print("Оценка дисперсии:", variance)
