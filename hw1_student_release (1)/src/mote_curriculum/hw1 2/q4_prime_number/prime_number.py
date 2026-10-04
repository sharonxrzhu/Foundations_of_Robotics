def is_prime_number(n):
    assert isinstance(n, int), "Did you cast to int in Q4.2?"
    """Return whether given integer is a prime_number.

    >>> is_prime_number(9)
    False
    >>> is_prime_number(2011)
    True

    """
    # BEGIN QUESTION 4.1
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True
    # END QUESTION 4.1
