import sys
sys.stdin = open('s_input.txt','r')

def DFS(start):
    v = [0]*(V+1)
    stack = []

    s = start
    v[s] = 1
    alst.append(s)

    while True :
        for e in range(1,V+1):
            if v[e] == 0 and adj[s][e] == 1 :
                stack.append(s)
                s = e
                v[s] = 1
                alst.append(s)
                break
        else :
            if stack != [] :
                s = stack.pop()
            else :
                break

T = int(input())
for test_case in range(1,T+1):
    V,E = map(int,input().split()) # V: 노드의 개수 E : 간선의 개수
    adj=[[0]*(V+1) for _ in range(V+1)]
    for _ in range(E) : # 노드들의 간선 정보
        s,e = map(int,input().split())
        adj[s][e] = 1
    S,G = map(int,input().split()) # S: 출발 노드, G: 도착 노드

    ans = 0 # 경로가 존재하면 1, 경로가 존재하지 않으면 0
    alst = []
    DFS(S)
    if G in alst :
        ans = 1
    print(f'#{test_case} {ans}')