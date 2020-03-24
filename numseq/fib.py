def memoize(func):
    memo = {}

    def inner(x):
        if x not in memo:
            memo[x] = func(x)
        return memo[x]
    return inner


@memoize
def fib(n):
    if n == 1 or n == 2:
        return 1
    else:
        return fib(n-1) + fib(n-2)