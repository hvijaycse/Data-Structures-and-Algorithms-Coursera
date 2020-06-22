# Uses python3
def partiton( array, start, end):
    pivot = array[start][0]
    j = start
    for i in range( start + 1, end + 1):
        if array[i][0] <= pivot:
            j += 1
            array[i], array[j] = array[j], array[i]
    array[start], array[j] = array[j], array[start]
    return j


def sort( array, start, end):
    if start >= end:
        return
    pivot =  partiton( array, start, end )
    sort( array, start, pivot )
    sort( array, pivot + 1, end)
    return

def find( array, point):
    start = 0
    end = len( array) - 1
    while start <= end:
        mid = ( start + end ) // 2
        if array[mid][0] <= point and point <= array[mid][1]:
            while array[mid][0] <= point and point <= array[mid][1]:
                mid = mid - 1
            return mid + 1
        if array[mid][0] > point:
            mid = end
        else:
            start = end
    return -1 


def fast_count_segments(ranges, points):
    cnt = [0] * len(points)
    #write your code here
    sort( ranges, 0 , len( ranges) - 1)
    for i, point in enumerate(points):
        index = find( ranges, point)
        print( index)
        if index == -1:
            continue
        count = 0
        while ranges[index][0] <= point and ranges[index][1] >= point:
            count +=1
            index += 1
        cnt[ i] = count
    return cnt


# def naive_count_segments(starts, ends, points):
#     cnt = [0] * len(points)
#     for i in range(len(points)):
#         for j in range(len(starts)):
#             if starts[j] <= points[i] <= ends[j]:
#                 cnt[i] += 1
#     return cnt

if __name__ == '__main__':
    n, m = map( int, input().split())
    ranges = []
    for i in range( n):
        ranges.append( list(map( int, input().split())))
    points = list( map( int, input().split()))[:m]
    #use fast_count_segments
    cnt = fast_count_segments( ranges, points)
    for x in cnt:
        print(x, end=' ')
