"""
Taylor series
"""
from typing import Union
import math
from itertools import count
constant = 0.000000001


def ex(x: Union[int, float]) -> float:
    """
    Calculate value of e^x with Taylor series

    :param x: x value
    :return: e^x value
    """
    total = 0
    n = 0
    while True:
        f_ex = (x ** n) / (math.factorial(n))
        n += 1
        total += f_ex
        if f_ex < constant:
            return total


def sinx(x: Union[int, float]) -> float:
    """
    Calculate sin(x) with Taylor series

    :param x: x value
    :return: sin(x) value
    """
    total = 0

    for n in count(0, 1):
        f_sin = ((-1) ** n) * ((x ** (2 * n + 1)) / (math.factorial(2 * n + 1)))
        total += f_sin
        if abs(f_sin) <= constant:
            return total

