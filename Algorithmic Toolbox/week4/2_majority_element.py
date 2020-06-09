

def get_majority_element(a, left, right):
    if left == right:
        return a[left]
    mid = ( left + right )//2
    left_majority = get_majority_element( a, left, mid  )
    right_majority = get_majority_element(a, mid + 1, right)
    if left_majority == right_majority :
        return left_majority
    else:
        left_count = 0
        right_count = 0
        for element in a[left : right + 1]:
            if element == left_majority:
                left_count +=1 
            if element == right_majority:
                right_count += 1
        if left_count > right_count:
            return left_majority
        else:
            return right_majority

if __name__ == '__main__':
    n = int( input())
    a = list(map(int, input().split()))
    ans = get_majority_element( a , 0, n-1)
    count = 0
    for i in a :
        if i == ans :
            count += 1
    if count > n/2:
        print( 1)
    else:
        print(0)

