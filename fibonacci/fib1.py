def fib(n: int) -> int:
    if n < 2:
        return n
    return fib(n-1) + fib(n-2)


if __name__ == "__main__":
    print(fib(4))


# Down Sides of this approach
"""
Since each fib(n) call results to two function call for fib(n-1) and fib(n-2),
it grows exponentially.
For eg: fib(5) -> fib(4) and fib(3)
        fib(4) -> fib(3) and fib(2)
        fib(3) -> fib(2) and fib(1)
        fib(2) -> fib(1) and fib(0)
        fib(2) -> fib(1) and fib(0)
        fib(1) -> 1
        fib(1) -> 1
        fib(0) -> 0
        fib(0) -> 0

Here if we see, there are total 9 call to fib() just to compute value for 4.
"""
