# Uses python3
import sys

def optimal_summands(n):
    summands = [0]
    i = 1
    #write your code here
    while i <= n :
        summands.append( i)
        n = n - i
        i += 1
    if n :
        summands[-1] = summands[-1] + n
    return summands[1:]

if __name__ == '__main__':
    n = int(input())
    summands = optimal_summands(n)
    print(len(summands))
    for x in summands:
        print(x, end=' ')
