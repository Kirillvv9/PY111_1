from typing import Sequence, Optional


def binary_search(elem: int, arr: Sequence, left_ = None, right_ = None) -> Optional[int]:
    """
    Performs binary search of given element inside of array (using recursive way)
    :param elem: element to be found
    :param arr: array where element is to be found
    :return: Index of element if it's presented in the arr, None otherwise
    """
    if left_ is None:
        left_ = 0  # задаем левую границу, если не задана
    if right_ is None:
        right_ = len(arr) - 1  # задаем правую границу, если не задана
    middle_ = left_ + (right_ - left_) // 2  # определили индекс центра

    if left_ > right_:
        return None
    if arr[middle_] == elem:
        first_elem = arr.index(elem)
        return first_elem
    if arr[middle_] < elem:
        left_ = middle_ + 1
        return binary_search(elem, arr, left_, right_)
    if arr[middle_] > elem:
        right_ = middle_ - 1
        return binary_search(elem, arr, left_, right_)








