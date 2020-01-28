from copy import deepcopy


def linear(x, n=1):
    assert n >= 1
    return x + n


def polynomial(x, n=2):
    assert n > 1
    return x ** n


def exp(x, n=2):
    assert n > 1
    return n ** x


def tetrate(x, n=2):
    assert n > 1
    if x == 0:
        return 1
    return n ** (tetrate(x - 1, n))


def _ackermann(m, n):
    if m == 0:
        return n + 1
    elif m > 0 and n == 0:
        return _ackermann(m - 1, 1)
    else:
        return _ackermann(m - 1, _ackermann(m, n - 1))


def ack_simple(n):
    return _ackermann(n, n)
