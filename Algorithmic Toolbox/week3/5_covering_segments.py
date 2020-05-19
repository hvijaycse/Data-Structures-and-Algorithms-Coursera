# Uses python3
import sys
def takeSecond(elem):
    return elem[1]

def optimal_points(segments):
    points = []
    #write your code here
    segments.sort( key = takeSecond)
    point = -1
    for segment in segments:
        if point < segment[0]:
            point = segment[1]
            points.append(point)
    return points

if __name__ == '__main__':
    n = int( input())
    segments = []
    for i in range( n):
        a,b = map( int, input().split())
        segments.append([a,b])
    points = optimal_points(segments)
    print(len( points))
    for i in points:
        print( i , end = ' ')