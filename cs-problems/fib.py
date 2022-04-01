def fib(i: int) -> int:
    if i < 2: return i
    return fib(i - 2) + fib(i - 1)


if __name__ == "__main__":
    print(fib(3))
