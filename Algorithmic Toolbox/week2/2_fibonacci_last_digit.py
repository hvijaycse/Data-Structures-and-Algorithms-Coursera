# Uses python3

def get_fibonacci_last_digit_naive(n):
    if n <= 1:
        return n
    first = 0
    second = 1
    while( n - 1 ):
        n -= 1
        temp = first + second
        first = second % 10
        second = temp % 10

    return second 

if __name__ == '__main__':
    n = int(input())
    print(get_fibonacci_last_digit_naive(n))
