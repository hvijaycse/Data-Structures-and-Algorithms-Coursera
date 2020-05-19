# Uses python3
import sys

def get_optimal_value(capacity, weights, values):
    value = 0.0
    v_w = []
    for v, w in zip( values, weights):
        v_w.append( (v/w, w))
    v_w.sort( reverse= True)
    i =0
    max_i = len( v_w)
    while capacity and i < max_i:
        factor = capacity / v_w[i][1]
        if factor > 1 :
            factor = 1
        value += v_w[i][0] * v_w[i][1] * factor
        capacity -= v_w[i][1] * factor
        i += 1
    return value


if __name__ == "__main__":
    data = list(map(int, input().split()))
    n, capacity = data[0:2]
    values = []
    weights = []
    for i in range(n):
        v, w = map( int, input().split())
        values.append(v)
        weights.append(w)
    opt_value = get_optimal_value(capacity, weights, values)
    print("{:.4f}".format(opt_value))
