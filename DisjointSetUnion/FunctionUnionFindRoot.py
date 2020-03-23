def root(Arr,i):
    while(Arr[ i ] != i):
        Arr[ i ] = Arr[ Arr[ i ] ]
        i = Arr[ i ]
    return i
def weighted_union(Arr,size,A,B):
    root_A = root(Arr,A)
    root_B = root(Arr,B);
    if root_A!=root_B:
        if(size[root_A] < size[root_B ]):
            Arr[ root_A ] = Arr[root_B]
            size[root_B] += size[root_A]
        else:
            Arr[ root_B ] = Arr[root_A]
            size[root_A] += size[root_B]
def find(Arr,A,B):
    if( root(Arr,A)==root(Arr,B) ) :
        return True
    else:
        return False