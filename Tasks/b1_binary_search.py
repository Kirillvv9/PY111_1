from typing import Sequence, Optional


def binary_search(elem: int, arr: Sequence) -> Optional[int]:
    """
    Performs binary search of given element inside of array

    :param elem: element to be found
    :param arr: array where element is to be found
    :return: Index of element if it's presented in the arr, None otherwise
    """

    left_ = 0  # левая граница
    right_ = len(arr) - 1  # правая граница

    while left_ <= right_:
        middle_ = (left_ + right_) // 2  # центр
        middle_e = arr[middle_]  # назначили центральный

        if middle_e == elem:
            return middle_

        elif middle_e > elem:
            right_ = middle_ - 1
        else:
            left_ = middle_ + 1

    print(elem, arr)
    return None


if __name__ == "__main__":
    arr = [i for i in range(1, 99)]
    elem = 5
    print(binary_search(elem, arr))
