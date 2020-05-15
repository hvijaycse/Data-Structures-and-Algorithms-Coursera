# Uses python3

def gcd_naive(a, b):
    while a:
        a , b = b%a, a
    return b
    
if __name__ == "__main__":
    a, b = map(int, input().split())
    print(gcd_naive(a, b))
