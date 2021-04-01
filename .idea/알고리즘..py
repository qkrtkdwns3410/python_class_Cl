n =int(input())
alist =[]
blist=[]
for i in range(n):
    alist.append(list(map(str,input().split())))
low =int(input())
high =int(input())
for i in alist:
    cut = int(i[1][-3:])
    if low<=cut<=high:
        blist.append(tuple(i))
print(blist)
