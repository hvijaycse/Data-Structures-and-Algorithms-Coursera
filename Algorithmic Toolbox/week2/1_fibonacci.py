# Uses python3
def calc_fib(n):
    if (n <= 1):
        return n
    first = 0
    second = 1
    while( n - 1 ):
        n -= 1
        temp = first + second
        first = second
        second = temp
    return second

n = int(input())
print(calc_fib(n))
