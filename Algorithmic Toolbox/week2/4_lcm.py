# Uses python3

def lcm_naive(a, b):
    if b > a:
        maximum = b
    else:
        maximum = a
    l = maximum
    while True:
        if l %a ==0 and l%b == 0 :
            return l 
        else:
            l += maximum
    return a*b

if __name__ == '__main__':
    a, b = map(int, input().split())
    print(lcm_naive(a, b))

