#!/home/fode4cun/.local/share/virtualenvs/checkio-ufRDicT7/bin/checkio --domain=py run is-even

# Check if the given number is even or not. Your function should return True if the number is even, and False if the number is odd.
# 
# Input:An int.
# 
# Output:A bool.
# 
# Precondition:both given ints should be between -1000 and 1000
# 
# 
# END_DESC

def is_even(num: int) -> bool:
    return True if num % 2 == 0 else False


if __name__ == '__main__':
    print("Example:")
    print(is_even(2))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert is_even(2) == True
    assert is_even(5) == False
    assert is_even(0) == True
    print("Coding complete? Click 'Check' to earn cool rewards!")
