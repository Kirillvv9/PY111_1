from typing import List


def sort(container: List[int]) -> List[int]:
    """
    Sort input container with merge sort

    :param container: container of elements to be sorted
    :return: container sorted in ascending order
    """
    if len(container) > 1:
        middle_ = len(container) // 2
        left_ = container[:middle_]
        right_ = container[middle_:]

        sort(left_)
        sort(right_)

        i = 0
        j = 0
        k = 0
        while i < len(left_) and j < len(right_):
            if left_[i] < right_[j]:
                container[k] = left_[i]
                i = i + 1
            else:
                container[k] = right_[j]
                j = j + 1
            k = k + 1

        while i < len(left_):
            container[k] = left_[i]
            i = i + 1
            k = k + 1

        while j < len(right_):
            container[k] = right_[j]
            j = j + 1
            k = k + 1
    return container

