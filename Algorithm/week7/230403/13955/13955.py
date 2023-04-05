import sys
sys.stdin = open('s_input.txt','r')

def BFS(start):
    global alst
    s = start
    v[s] = 1
    q = [s]
    alst.append(s)

    while q :
        c = q.pop(0)
        for e in adj[c]:
            if v[e] == 0 :
                v[e] = 1
                q.append(e)
                alst.append(e)

    return
T = int(input())
for tc in range(1,T+1):
    N,E = map(int,input().split())

    adj = [[] for _ in range(N+1)]
    for _ in range(E):
        s,e = map(int,input().split())
        adj[s].append(e)
        adj[e].append(s)

    v = [0]*(N+1)
    alst = []
    BFS(1)
    print(f'#{tc}', *alst)