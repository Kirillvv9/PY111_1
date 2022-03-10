def check_brackets(brackets_row: str) -> bool:

    """
    Check whether input string is a valid bracket sequence
    Valid examples: "", "()", "()()(()())", invalid: "(", ")", ")("
    :param brackets_row: input string to be checked
    :return: True if valid, False otherwise
    """
    left_ = brackets_row.count('(')
    right_ = brackets_row.count(')')
    if left_ == right_ and brackets_row.startswith(')') == False or left_ == 0 and right_ == 0:
        return True
    else:
        return False



