# python3
import sys


def compute_min_refills(distance, tank, stops):
    # write your code here
    count = 0
    start = 0
    stops = [0]+ stops + [distance]
    final = len( stops) - 1
    i = 0 
    base = tank
    while i < final:
        if stops[i + 1] - stops[i] > tank:
            return -1
        i += 1
    while start < final:
        while start < final and stops[start + 1] <= tank:
            start += 1
        if start == final:
            break
        count += 1
        tank = stops[start] + base
    return count



if __name__ == '__main__':
    d = int( input())
    m = int(input())
    _ = int( input())
    stops = list( map( int, input().split() ) )
    print(compute_min_refills(d, m, stops))
