# Uses python3
def fibonacci_sum_squares_naive(n):
    if n <= 1:
        return n
    previous = 0
    current  = 1
    sum1      = 1
    for _ in range(n - 1):
        previous, current = current, previous + current
        previous, current = previous % 10, current % 10 
        sum1 = ( sum1 + current* current) % 10
    return sum1
    
if __name__ == '__main__':
    n = int(input())
    print(fibonacci_sum_squares_naive(n))
