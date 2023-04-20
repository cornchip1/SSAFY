def dfs(n,tmp):
    if n == 6 :
        if sorted(tmp) not in alst:
            alst.append(tmp)
        return
    for i in range(k):
        if v[i] == 0 :
            v[i] = 1
            if len(tmp) > 0:
                if lst[i] > tmp[-1]:
                    dfs(n+1,tmp+[lst[i]])
            else: dfs(n+1,tmp+[lst[i]])
            v[i] = 0

while True:
    INPUT = list(map(int,input().split()))
    if INPUT == [0] : break
    else:
        k = INPUT[0]
        lst = INPUT[1:]
        alst, v = [], [0]*k
        dfs(0,[])

        for a in alst:
            print(*a)
        print('')