t =int(input())
sum=0
for i in range(t):
    sum=0
    a =list(map(int,input().split()))
    for j in a:
        if j %2 ==0:
            pass
        else:
            sum +=j
    print("#%d %d"%((i+1),sum))
