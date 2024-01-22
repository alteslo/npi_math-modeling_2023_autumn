import numpy as np
from scipy.stats import kurtosis, skew


def load_data():
    with open("data.txt", "r") as file:
        return list(map(float, file.read().splitlines()))


def calculate_stat():

    data = load_data()

    # Вычисление статистических характеристик
    mean = np.mean(data)    # выборочное среднее
    variance = np.var(data)  # оценка дисперсии
    skewness = skew(data)   # коэффициент асимметрии
    kurt = kurtosis(data)   # эксцесс

    return (f"Среднее значение: {mean}\n" +
            f"Оценка дисперсии: {variance}\n" +
            f"Коэффициент асимметрии: {skewness}\n" +
            f"Эксцесс: {kurt}")


if __name__ == "__main__":
    print(calculate_stat())
