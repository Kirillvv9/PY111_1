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
    min_element_index = 0
    for i, elem in enumerate(arr):
        if elem < min_element:
            min_element = elem
            min_element_index = i
    print(arr)

    return min_element_index


