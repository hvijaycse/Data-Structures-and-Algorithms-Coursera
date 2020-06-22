#Uses python3
def lcs2(a, b):
    #write your code here
    a.reverse()
    b.reverse()
    m = len( a )
    n = len( b )
    dp = [[0 for x in range(n + 1)] for x in range(m + 1)] 
    direction = [[0 for x in range(n + 1)] for x in range(m + 1)] 
    for i in range(1, m + 1): 
        for j in range(1, n + 1): 
            if i == 0: 
                dp[i][j] = j
            elif j == 0: 
                dp[i][j] = i     
            elif a[i-1] == b[j-1]: 
                dp[i][j] = dp[i-1][j-1]  + 1
                direction[i][j] = 'c'
            else: 
                maximum = dp[i][j -1]
                d = 'L'
                if maximum < dp[i -1][j]:
                    d = 'U'
                if maximum < dp[i-1][j -1]:
                    d = 'd'
                dp[i][j] = maximum
                direction[i][j] = d  
    print( [0, 0] + b)
    print( [0]+  direction[0])
    for i in range(1, m + 1):
        print([a[i- 1]]+ direction[i] )
    return dp[m][n]

if __name__ == '__main__':
    n = input()
    a = list( map( int, input().split()))
    m = input()
    b = list( map( int, input().split()))
    print(lcs2(a, b))
