import math
from sympy import *


def plot_function(fun, left: float, right: float, dx: float):
    height = 15
    x = left
    while x <= right:
        y = fun.subs("x", x)
        scaled_y = int(y * height)
        line = " " * (scaled_y + height) + "*"
        print(line)
        x += dx


if __name__ == "__main__":
    str_fun: str = input("Введите функцию (вместе с переменной): ")
    minx: float = float(input("Введите минимальное значение x: "))
    maxx: float = float(input("Введите максимальное значение x: "))
    dx: float = float(input("Введите шаг: "))
    try:
        func = sympify(str_fun)
    except SympifyError:
        print("Неверный формат функции")
        exit(1)

    plot_function(func, minx, maxx, dx)
