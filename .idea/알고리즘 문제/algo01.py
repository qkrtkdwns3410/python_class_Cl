from itertools import groupby

a=list(map(int,input().split()))
def sum_consecutives(s):
    return [sum(v) for i,v in groupby(s)]
print(sum_consecutives(a))