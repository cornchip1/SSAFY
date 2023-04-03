import sys
sys.stdin = open('s_input.txt','r')

def dfs(start,alst):

    s = start
    v[s] = 1

    if s == N :

        return alst

    for i in adj[s]:
        if v[i] == 0 :
            v[i] = 1
            alst.append(adj[s][i])
            dfs(i,alst)
            v[i] = 0


T = int(input())
for tc in range(1,T+1):
    N,E = map(int,input().split())
    adj = [[] for _ in range(N+1)]
    v = [0]*(N+1)

    for _ in range(E):
        s,e = map(int,input().split())
        adj[s].append(e)
        adj[e].append(s)

    dfs(1,[1])

    print(f'#{tc} {dfs(1,[])}')