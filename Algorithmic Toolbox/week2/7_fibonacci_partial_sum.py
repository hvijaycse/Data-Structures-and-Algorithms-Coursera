import random

def fibonacci_partial_sum_naive(from_, to):
    sum = 0
    current = 0
    next  = 1
    for i in range(to + 1):
        if i >= from_:
            sum = sum + current
        current, next = next  ,current + next 
    return sum % 10

def fibonacci_sum_naive(n, m ):
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
        start =  9
    else:
        start =  series[index] -1 
    
    index = (m % length) + 2 
    index = index % length
    if not series[index]:
        end =  9
    else:
        end =  series[index] -1
    
    if end - start < 0 :
        return 9 - (end - start)
    else:
        return end - start

if __name__ == '__main__':
    while True:
        from_, to = random.randint( 0, 100), random.randint(101, 1000)
        ans1 = fibonacci_partial_sum_naive(from_, to)
        ans2 = fibonacci_sum_naive( from_, to)
        if ans1 == ans2:
            print( "ok")
        else:
            print( from_, to, ans1, ans2)
            break