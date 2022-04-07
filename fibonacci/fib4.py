# Uses iterative approach and even more performant

def fib(n: int) -> int:
    if n == 0:
        return n
    last: int = 0
    next: int = 1
    for _ in range(1, n):
        last, next = next, last+next # tuple unpacking
    return next


if __name__ == "__main__":
    print(fib(0))
