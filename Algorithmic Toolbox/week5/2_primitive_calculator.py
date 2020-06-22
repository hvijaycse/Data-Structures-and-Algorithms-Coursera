# Uses python3

def optimal_sequence(n):
    sequence =[-1]*( n + 3)
    operation = [1]*( n + 3)
    sequence[0], sequence[1], sequence[2], sequence[3] = 0, 1, 2, 2
    operation[0], operation[1], operation[2], operation[3] = 0, 1, 2, 3
    for i in range( 4, n + 1):
        min_1 = sequence[i - 1] + 1
        div_2 = sequence[i //2] + i %2 + 1
        div_3 = sequence[i //3] + i %3 + 1
        min_step = float('inf')
        min_operation = 1
        if min_step > min_1 :
            min_step = min_1
            min_operation = 1
        if min_step > div_2:
            min_step = div_2
            min_operation = 2
        if min_step > div_3:
            min_step = div_3
            min_operation = 3

        sequence[i] = min_step
        operation[i] = min_operation
    # print( sequence[n])
    return_Sequence = []
    while n :
        return_Sequence.append(n)
        if operation[n] == 1:
            n = n - 1
        elif operation[n] == 2:
            if n %2 :
                return_Sequence.append( n - 1)
            n = n//2
        else:
            k = n %3
            while k :
                n = n - 1
                k = k - 1
                return_Sequence.append(n)
            n = n //3
    return_Sequence.reverse()
    return return_Sequence



def main():
    n = int(input())
    sequence = optimal_sequence(n)
    print(len(sequence) - 1)
    for x in sequence:
        print(x, end=' ')

if __name__ == "__main__":
    main()
    exit(0)
