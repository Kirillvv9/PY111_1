"""
This module implements some functions based on linear search algo
"""
from typing import Sequence


def min_search(arr: Sequence) -> int:
    """
    Function that find minimal element in array

    :param arr: Array containing numbers
    :return: index of first occurrence of minimal element in array
    """
    min_element = arr[0]
    index = -1
    for i in arr:
        if i < min_element:
            min_element = i
            index += 1
        else:
            index += 1
            continue

    print(arr)
    return index

