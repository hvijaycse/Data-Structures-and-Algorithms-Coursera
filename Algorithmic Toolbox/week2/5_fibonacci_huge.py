# Uses python3

def get_fibonacci_huge_naive(n, m):
    if n <= 1:
        return n
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
    Length = len( sequense)
    return sequense[ n % Length]

    
if __name__ == '__main__':
    n, m = map(int, input().split())
    print(get_fibonacci_huge_naive(n, m))
