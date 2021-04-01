a= int(input())
alist = list(map(str,input().split()))
removeA =input()
removeIndex = int(input())
count=0
for i,v in enumerate(alist):
    if v == removeA:
        count+=1
        if count == removeIndex:
            alist.pop(i)
            break
print(alist)

