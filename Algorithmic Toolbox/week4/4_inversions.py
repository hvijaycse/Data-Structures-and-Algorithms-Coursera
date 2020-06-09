# Uses python3
import sys

def Merge( Left, Right):
    array = []
    l_max = len( Left)
    r_max = len( Right)
    l = 0 
    r = 0
    inversion = 0 
    while r < r_max and l < l_max:
        if Left[l] <= Right[r]:
            array.append( Left[l])
            l += 1
        else:
            array.append( Right[r])
            inversion += len(Left) - l
            r += 1
    if l < l_max:
        array += Left[l:]
    if r < r_max:
        array += Right[r:]
    return array, inversion

def get_number_of_inversions( array, start, end , inversion):
    if start == end:
        return [array[start]], inversion
    mid = ( start + end ) // 2
    left_array , left_inversion = get_number_of_inversions( array, start, mid, inversion)
    right_array, right_inversion = get_number_of_inversions( array, mid + 1, end, inversion)
    inversion +=  left_inversion
    inversion += right_inversion
    array , N_inversion = Merge( left_array, right_array)
    inversion += N_inversion
    return array, inversion

def main():
    n = int( input())
    a = list(map(int, input().split()))[: n]
    no_of_inversions = get_number_of_inversions(a, 0, n - 1, 0 )[1]
    print(no_of_inversions)

if __name__ == '__main__':
    main()
    
