def dfs1(v,k): # 중복 없이, 빠짐 없이
    visited[v] = 1 # 중복 방지
    print(v)

    for w in range(1,k+1):
        if adjM[v][w] == 1  and visited[w] == 0 :
            dfs1(w,k)

V, E = map(int,input().split())
arr = list(map(int,input().split()))
adjM = [[0]*(V+1) for _ in range(V+1)]
adjL = [[] for _ in range(V+1)]
for i in range(E):
    n1,n2 = arr[i*2],arr[i*2+1]
    adjM[n1][n2] = 1
    adjM[n2][n1] = 1
    adjL[n1].append(n2)
    adjL[n2].append(n1)

visited = [0]*(V+1) # 중복 방지
dfs1(1,V)