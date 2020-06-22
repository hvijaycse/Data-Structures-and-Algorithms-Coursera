# Uses python3

def get_change(m):
    #write your code here
    arr = [0,1,2,1,1]
    for num in range( 5, m + 1):
        min_count = float( 'inf')
        for i in range ( 1, (num//2 )+ 1):
            curr_count = arr[i] + arr[num -i]
            if curr_count < min_count:
                min_count = curr_count
        arr.append( min_count)
    return arr[m]

if __name__ == '__main__':
    m = int(input())
    print(get_change(m))
    exit(0)
