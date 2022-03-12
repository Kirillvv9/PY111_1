def check_brackets(brackets_row: str) -> bool:

    """
    Check whether input string is a valid bracket sequence
    Valid examples: "", "()", "()()(()())", invalid: "(", ")", ")("
    :param brackets_row: input string to be checked
    :return: True if valid, False otherwise
    """
    n = 0  # будем считать число скобочек
    for i in brackets_row:
        if i == '(':
            n += 1
        elif i == ')':
            n -= 1  # в итоге должен быть 0
            if n < 0:  # если находится одна закрывающая скобка перед открывающей, то False
                break
    if n == 0:
        return True
    else:
        return False



