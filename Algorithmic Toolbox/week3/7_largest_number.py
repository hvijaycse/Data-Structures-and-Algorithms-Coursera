#Uses python3
def is_greater_or_equal( a , b):
    return int( a+b) >= int(b + a)

def largest_number(data):
    answer = []
    while data:
        maxi =data[0]
        for digit in data:
            if is_greater_or_equal( digit, maxi):
                maxi = digit
        answer.append( maxi)
        data.remove( maxi)
    return ''.join( answer)
if __name__ == '__main__':
    n = int(input())
    data = input().split()
    print(largest_number(data))
    
