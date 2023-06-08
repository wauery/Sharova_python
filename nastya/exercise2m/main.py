import numpy as np
from typing import List, Final


SAMPLE_URL: Final[str] = \
    "https://raw.githubusercontent.com/mathling-programming/practice2022/main/exercise2m/sample.csv"


if __name__ == '__main__':
    data = np.genfromtxt(SAMPLE_URL, delimiter=',')
    new_data: List[List[float]] = []
    for i in range(len(data)):
        avg = np.average(data[i])
        std = np.std(data[i])
        new_data.append([i + 1, avg, std])

    new_data = list(filter(lambda x: x[2] < 250, new_data))
    np.savetxt("output.txt", new_data, delimiter="\t", fmt="%.2f")