import sys
sys.stdin = open('s_input.txt','r')

def DFS(S):

    v = [0]*(V+1)
    stk = []

    s = S
    v[s] = 1
    alst.append(s)

    while True :
        for e in adj[s] : #연결된 노드
            if v[e] == 0 : # 미방문 노드
                stk.append(s)
                s = e
                v[s] = 1
                alst.append(s)
                break
        else : # 연결 안됨
            if stk : s = stk.pop()
            else : break


T = int(input())
for test_case in range(1,T+1):
    V, E = map(int,input().split())
    adj = [[] for _ in range(V+1)]
    for _ in range(E):
        s,e = map(int,input().split())
        adj[s].append(e)
    S,G = map(int,input().split())
    alst = []
    DFS(S)
    ans = 0
    if G in alst : ans = 1
    print(f'#{test_case} {ans}')