# Uses python3

def binary_search(a, x, low, high ):
    # print( low, high)
    if low > high :
        return -1
    elif low == high:
        if a[low] == x:
            return low

    # write your code here
    mid = (low + high ) //2
    if a[mid] == x:
        return mid
    elif x < a[mid]:
        return binary_search( a , x ,low, mid-1)
    else:
        return binary_search( a, x, mid + 1, high)

def linear_search(a, x):
    for i in range(len(a)):
        if a[i] == x:
            return i
    return -1

if __name__ == '__main__':
    line1 = list(map(int, input().split()))
    line2 = list( map( int, input().split()))
    n = line1[0]
    m = line2[0]
    a = line1[1:]
    for x in line2[1: ]:
        # replace with the call to binary_search when implemented
        print(binary_search(a, x, 0 , n - 1), end = ' ')
