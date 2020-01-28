from base import multilevel_sort
from index_functions import *

__ALL__ = ['worst_sort_basic', 'linear', 'polynomial', 'exponential', 'tetrate', 'ack_simple']

# Take function and modify it to return 0 at value 1
# And clamp it to range [0, +inf)
def _normalize_func(f):
    zero = f(1)

    def newfunc(x):
        res = f(x) - zero
        return 0 if res < 0 else res

    return newfunc


def worst_sort_basic(ll: list, f=linear):
    normalized = _normalize_func(f)

    return multilevel_sort(
        ll,
        f(len(ll))
    )

