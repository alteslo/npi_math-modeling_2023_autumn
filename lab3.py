import numpy as np
import pandas as pd
from scipy import stats


def load_data():
    with open("data.txt", "r") as file:
        return list(map(float, file.read().splitlines()))


def export_to_xls(intervals, probabilities):
    table = pd.DataFrame(
        {
            "Интервалы": intervals[:-1],
            "Теоретические частоты": probabilities
        }
    )
    table.to_excel("results.xlsx", index=False)
    print("Теоретические частоты попадания случайной величины в интервалы экспортированы в results.xlsx")


def calculate_occurrence():

    data = load_data()
    mean = np.mean(data)
    variance = np.var(data)

    _, bins = np.histogram(data, bins=len(np.unique(data)))
    probabilities = stats.norm.cdf(
        bins[1:], mean, variance**0.5) - stats.norm.cdf(bins[:-1], mean, variance**0.5)

    export_to_xls(bins, probabilities)

    print(
        f"Среднее значение: {mean}\n" +
        f"Оценка дисперсии: {variance}"
    )


if __name__ == "__main__":
    calculate_occurrence()
