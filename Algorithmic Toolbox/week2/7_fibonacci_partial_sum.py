def fibonacci_partial_sum_naive(from_, to):
    sum = 0
    current = 0
    next  = 1
    for i in range(to + 1):
        if i >= from_:
            sum = (sum + current )% 10
        current, next = next % 10 ,(current + next )% 10
    return sum 

if __name__ == '__main__':
    from_, to = map(int, input().split())
    print(fibonacci_partial_sum_naive(from_, to))