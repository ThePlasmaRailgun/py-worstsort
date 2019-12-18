"""
An implementation of the arbitrarily bad sorting algorithms defined in

'How inefficient can a sort algorithm be?' by Miguel A. Lerma.

https://sites.math.northwestern.edu/~mlerma/papers/inefficient_algorithms.pdf
"""

from copy import deepcopy


# Performs lexicographic comparison on arbitrarily nested integer lists
def lexicographic_lt(a, b):
    # They're integers!
    if type(a) != list:
        try:
            return a < b
        except:
            return NotImplementedError("Cannot compare values!")

    for i in range(len(a)):
        # a is less than b
        if lexicographic_lt(a[i], b[i]):
            return True
        # a is more than b
        elif lexicographic_lt(b[i], a[i]):
            return False
    # a == b
    return False


# Bubblesort naive sorting algorithm
# This is very basic and well documented online
def bubblesort(ll: list):
    for i in range(len(ll)):
        for j in range(1, len(ll) - i - 1):
            if lexicographic_lt(ll[j + 1], ll[j]):
                temp = deepcopy(ll[j])
                ll[j] = deepcopy(ll[j + 1])
                ll[j + 1] = temp
    return ll


# Return all permutations of a list
def list_perm(ll: list):
    if len(ll) <= 1:
        return [ll]
    else:
        # Permutations list
        p = []
        for i in range(len(ll)):
            # Make a copy
            l1 = deepcopy(ll)

            # Remove i-th element
            elem = l1.pop(i)

            # Generate all permutations of shortened list
            p0 = list_perm(l1)

            # Add them all back on to the front
            for perm in p0:
                p.append([elem] + perm)

        return p


def multilevel_sort(ll: list, depth):
    # If we are at minimum depth, use bubblesort!
    if depth == 0:
        return bubblesort(ll)

    # Otherwise, generate permutations, get the lexicographically first one by recursion, and use it.
    p = list_perm(ll)

    multilevel_sort(p, depth - 1)

    ll = p[1]

    return ll