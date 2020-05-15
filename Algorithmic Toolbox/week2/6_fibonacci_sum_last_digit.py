def fibonacci_sum_naive(n):
    previous = 0
    current = 1
    series = [0, 1]
    for i in range( 100 - 1):
        previous, current = current, current + previous
        cur = current % 10 
        if cur == 0:
            previous, current = current, current + previous
            cur2 = current % 10
            if cur2 == 1:
                break 
            else:
                series.append( cur)
                series.append(cur2)
        else:
            series.append(cur)
    length = len( series)
    index = (n % length) + 2 
    index = index % length
    if not series[index]:
        return 9
    else:
        return series[index] -1 

if __name__ == '__main__':
    n = int( input())
    print(fibonacci_sum_naive(n))
