# py-worstsort

An implementation of a recursive, extremely horrible sorting algorithm. It has arbitrarily bad Big-O complexity, just stick in an index function.

By default it's worse than iterated factorial, with just a LINEAR function. 

It also provides exponential, tetrational, and single-argument Ackermann function as indices (so it can even exceed primitive recursion).

I don't guarantee these will not break, they DEFINITELY are not production ready unless your prod environment runs on a computer with infinite time, and I don't guarantee any of these will work.

Have fun!


### Example: 

```python
from base.py import worst_sort_basic, tetrate

ll= [1, 3, 5, 7, 2]
# Absurdly bad sort, will stackoverflow. 
# Will also take longer than lifetime of universe if given the chance
sorted_list = sort_basic(ll, tetrate) 
```
