# A simple formatting function that adds comma separators to large numbers


def comma(number):
    """Adds a comma every three decimnal places to large numbers"""
    return("{:,}".format(number))
