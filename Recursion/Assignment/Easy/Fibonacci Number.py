# https://leetcode.com/problems/fibonacci-number/

def fib(n):
    if n == 0:
        return 0
    if n == 1:
        return 1

    return fib(m - 1) + fib(n - 2)

# With Memoization
def fib(n, mem={}):
    if n == 0:
        return 0
    if n == 1:
        return 1

    if n - 1 not in mem:
        mem[n-1] = fib(n - 1)
    if n- 2 not in mem:
        mem[n-2] = fib(n - 2)

    return mem[n - 1] + mem[n - 2]