# Uses python3

def get_fibonacci_huge_naive():
    m = 10
    previous = 0
    current  = 1
    sequense = [0, 1]
    while True:
        previous, current = current, previous + current
        s = current % m
        if s == 0:
            previous, current = current, previous + current
            s2 = current % m
            if s2 == 1:
                break
            else:
                sequense.append( s)
                sequense.append( s2)
                continue
        else:
            sequense.append(s)
    return sequense

def fibonacci_sum_squares_naive(n):
    series = get_fibonacci_huge_naive()
    length = len(series)
    a = series[ n % length]
    b = series[ (n + 1) % length]
    return (a*b) % 10
    
if __name__ == '__main__':
    n = int(input())
    print(fibonacci_sum_squares_naive(n))
