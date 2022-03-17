from typing import List


def sort(container: List[int]) -> List[int]:
    """
    Sort input container with bubble sort

    :param container: container of elements to be sorted
    :return: container sorted in ascending order
    """
    for i in range(len(container)):
        for j in range(len(container) - i - 1):
            if container[j] > container[j + 1]:                  # если порядок элементов пары неправильный
                container[j], container[j + 1] = container[j + 1], container[j]  # меняем элементы пары местами

    return container
