# 재귀호출을 이용하는 방법

import sys
sys.stdin = open('s_input.txt','r')

def dfs(s): # 나와 연결된 미방문 노드 탐색
    for e in adj[s] : #나와 연결된
        if v[e] == 0: # 방문하지 않은 노드
            v[e] = 1
            alst.append(e)
            dfs(e)

T = int(input())
for test_case in range(1,T+1):
    V,E = map(int,input().split())
    adj = [[] for _ in range(V+1)]
    for _ in range(E):
        s,e = map(int,input().split())
        adj[s].append(e)
        adj[e].append(s)

    alst = []
    v = [0]*(V+1)
    v[1]=1 # 시작지점은 방문 표시
    alst.append(1)
    dfs(1)

    print(f'#{test_case}', *alst)