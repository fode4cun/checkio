#!/home/fode4cun/.local/share/virtualenvs/checkio-ufRDicT7/bin/checkio --domain=py run sum-by-type

# You have a list. Each value from that list can be either a string or an integer. Your task here is to return two values. The first one is a concatenation of all strings from the given list. The second one is a sum of all integers from the given list.
# 
# Input:An array of strings ans integers
# 
# Output:A list or tuple
# 
# Precondition:both given ints should be between -1000 and 1000
# 
# 
# END_DESC

from typing import Tuple


def sum_by_types(items: list) -> Tuple[str, int]:
    text = ''
    count = 0

    for i in items:
        if isinstance(i, str):
            text += i
        else:
            count += i

    return text, count


if __name__ == '__main__':
    print("Example:")
    print(sum_by_types([]))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert sum_by_types([]) == ('', 0)
    assert sum_by_types([1, 2, 3]) == ('', 6)
    assert sum_by_types(['1', 2, 3]) == ('1', 5)
    assert sum_by_types(['1', '2', 3]) == ('12', 3)
    assert sum_by_types(['1', '2', '3']) == ('123', 0)
    assert sum_by_types(['size', 12, 'in', 45, 0]) == ('sizein', 57)
    print("Coding complete? Click 'Check' to earn cool rewards!")
