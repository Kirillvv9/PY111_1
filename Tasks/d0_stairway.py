from typing import Union, Sequence


def stairway_path(stairway: Sequence[Union[float, int]]) -> Union[float, int]:
    """
    Calculate min cost of getting to the top of stairway if agent can go on next or through one step.

    :param stairway: list of ints, where each int is a cost of appropriate step
    :return: minimal cost of getting to the top
    """

    stairs = len(stairway)  # считаем количесвто ступенейй
    for i in range(2, stairs):
        stairway[i] = stairway[i] + min(stairway[i - 1], stairway[i - 2])  # заменяем цену каждой ступени на
        # минимальную стоимость подхода к ней ([1, 10, 5, 11] -> [1, 10, 6 (5 + 1), 11]...)
    return stairway[-1]  # получился новый список, где последний элемент - минимальная стоимость прохода по лестнице
