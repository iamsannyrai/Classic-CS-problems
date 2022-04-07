# Uses memoization technique by using built in decorator for memoizing
from functools import lru_cache


@lru_cache
def fib(n: int) -> int:
    if n < 2:
        return n
    else:
        return fib(n-2) + fib(n-1)


if __name__ == "__main__":
    print(fib(4))


"""
    In python 3.9, there is another decorator called cache(), which returns the same as lru_cache(maxsize=None).
    But faster than lru_cache() with a size limit.
"""