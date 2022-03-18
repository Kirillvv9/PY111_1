"""
Taylor series
"""
from typing import Union

from itertools import count
constant = 0.000000001


def ex(x: Union[int, float]) -> float:
    """
    Calculate value of e^x with Taylor series

    :param x: x value
    :return: e^x value
    """
    total = 0
    a = b = 1

    for n in count(1, 1):
        current_item = a / b
        total += current_item
        if abs(current_item) < constant:
            return total
        a = a * x
        b = b * n


def sinx(x: Union[int, float]) -> float:
    """
    Calculate sin(x) with Taylor series

    :param x: x value
    :return: sin(x) value
    """
    total = 0
    a = b = 1
    per = x

    for n in count(3, 2):
        current_item = a * per / b
        total += current_item
        if abs(current_item) < constant:
            return total
        a = -a
        b = b * n * (n - 1)
        per = per * (x ** 2)

