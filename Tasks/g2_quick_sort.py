from typing import List
import random


def sort(container: List[int]) -> List[int]:
    """
    Sort input container with quick sort

    :param container: container of elements to be sorted
    :return: container sorted in ascending order
    """
    if len(container) <= 1:
        return container
    else:
        q = random.choice(container)  # выбираем случайную опорную точку
        L = []
        M = []
        R = []
        for elem in container:
            if elem < q:  # все, что меньше опорной точки заносим сюда
                L.append(elem)
            elif elem > q:  # все, что больше опорной точки заносим сюда
                R.append(elem)
            else:
                M.append(elem)  # все, что равно опорной точке заносим сюда
        return sort(L) + M + sort(R)

