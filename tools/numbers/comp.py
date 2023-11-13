def sum_of_digits(n):
    result = sum(int(num) for num in str(n)) 
    return f"Sum of digits of {n}: {result}"


def print_number_and_reverse(n):
    original = str(n)
    reversed_str = original[::-1]
    if original == reversed_str:
        return f"The number {n} is a palindrome."
    else:
        return f"Original: {original}, Reversed: {reversed_str}"
