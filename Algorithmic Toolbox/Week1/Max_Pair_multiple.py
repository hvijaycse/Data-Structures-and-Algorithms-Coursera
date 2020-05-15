
def Max_Product( Array):
    Max_index1 = 0
    Max_Value1 = 0
    Max_Value2 = 0
    for index, value in enumerate( Array):
        if value > Max_Value1 :
            Max_Value1 = value
            Max_index1 = index
    for index , value in enumerate( Array):
        if value > Max_Value2 and index != Max_index1:
            Max_Value2 = value
        
    return Max_Value1 * Max_Value2

if __name__ == "__main__":
    N = int( input())
    Array = list( map( int, input().split()))[:N]
    print( Max_Product( Array))
    exit(0)    