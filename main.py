def isOdd(n):
    if isinstance(n, int) and not isinstance(n, bool):
        return n % 2 != 0
    return False
