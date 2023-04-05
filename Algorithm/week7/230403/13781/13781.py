import sys
sys.stdin = open('s_input.txt','r')

def DFS(start):
    global alst

    s = start
    v[s] = 1
    alst.append(s)

    for e in adj[s]:
        if v[e] == 0 : # 미방문
            v[e] = 1
            s = e
            DFS(s)
    return

T = int(input())
for tc in range(1,T+1):
    N, E = map(int,input().split())
    adj = [[] for _ in range(N+1)]
    for _ in range(E):
        s,e = map(int,input().split())
        adj[s].append(e)
        adj[e].append(s)

    v = [0] * (N+1)
    alst = []
    DFS(1)
    print(f'#{tc}', *alst)