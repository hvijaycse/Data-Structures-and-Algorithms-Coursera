# Uses python3
import sys

def get_change(m):
    #write your code here
    coins = [10,5,1]
    i = 0
    count = 0
    while m :
        if m >= coins[i]:
            count += m // coins[i]
            m = m % coins[i]
        i = i  + 1
    return count

if __name__ == '__main__':
    m = int(input())
    print(get_change(m))
