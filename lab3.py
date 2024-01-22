from typing import Iterable
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats
import pandas as pd


"""
    Необходимо добавить возможность вычисление вероятности попадания исследуемой случайной величины
X , координаты которых определены ранее. Результаты вычислений свести в таблицу excell, где имя первого столбца "Границы Интервалов", а второго "Теоретические Частоты"

"""


def save_data(data: Iterable):
    with open("data.txt", "w") as file:
        for item in data:
            file.write("%s\n" % item)


def get_data():
    YES, NO, QUIET = "y", "n", "q"

    while True:
        print("Сгенерировать данные для обработки?")
        choice = input("Если да введите: 'y', если нет введите 'n'\n")

        if choice == YES:
            data = np.random.normal(loc=5, scale=2, size=1000)
            break
        elif choice == NO:
            data = input("Введите числа, разделенные пробелами: ").split()
            data = list(map(float, data))
            break
        elif choice == QUIET:
            return None
        else:
            print("Некорректный выбор. Пожалуйста, повторите ввод.")

    return data


def show_stat_plot(data: Iterable, mean: float, variance: float):
    plt.figure(figsize=(20, 10))
    # Построение эмпирического закона распределения
    plt.subplot(131)
    plt.title('Эмпирический закон случайной величины')
    xmin, xmax = plt.xlim()
    x = np.linspace(xmin, xmax, 100)
    p = stats.norm.pdf(x, mean, variance**0.5)
    plt.plot(x, p, 'k', linewidth=2)

    # Построение гистограммы
    plt.subplot(132)
    plt.title('Гистограмма')
    plt.hist(data, bins=len(np.unique(data)), edgecolor='black')

    # Построение функции распределения
    plt.subplot(133)
    plt.title('Функция распределения')
    plt.plot(x, stats.norm.cdf(x, mean, variance**0.5), 'r', linewidth=2)
    plt.show()


def calculate_stat():

    data = get_data()
    if data is None:
        return "Вы решили не вводить данные. Программа завершена."

    save_data(data)

    # Вычисление статистических характеристик
    mean = np.mean(data)    # выборочное среднее
    variance = np.var(data)  # оценка дисперсии

    # Calculate probabilities
    # Customize the range and step according to your needs
    intervals, bins = np.histogram(data, bins='auto')
    probabilities = stats.norm.cdf(
        bins[1:], mean, variance**0.5) - stats.norm.cdf(bins[:-1], mean, variance**0.5)

    # Create Excel table
    table = pd.DataFrame(
        {"Интервалы": bins[:-1], "Теоретические частоты": probabilities})
    table.to_excel("results.xlsx", index=False)


    show_stat_plot(data, mean, variance)

    return (f"Среднее значение: {mean}\n" +
            f"Оценка дисперсии: {variance}")


if __name__ == "__main__":
    print(calculate_stat())
