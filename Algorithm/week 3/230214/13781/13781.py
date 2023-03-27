import sys
sys.stdin = open('s_input.txt','r')

def DFS(start):
    visited = [0]*(V+1)
    stack = []

    # start from givien initial point
    s = start
    visited[s] = 1
    alst.append(s)

    #
    while True:
        for e in range(1,V+1):
            if visited[e] == 0 and adj[s][e] == 1 : # 방문한 적 없고, s와 연결되어 있다면
                stack.append(s)
                s = e
                visited[s] = 1
                alst.append(s)
                break # 새로운 시작점에서 출발해야 하므로 for 탈출
        else : # 방문한 적 있다면
            if stack != [] : # stack이 비어있지 않다면
                s = stack.pop() # stack의 맨 마지막 원소가 시작점이 된다
            else :
                break # stack 이 비어있으면 그만둔다


T = int(input())
for test_case in range(1,T+1):
    V, E = map(int,input().split()) # V: 노드의 개수 E: 간선 정보
    adj = [[0]*(V+1) for _ in range(V+1)]
    for _ in range(E):
        s,e = map(int,input().split())
        adj[s][e] = adj[e][s] = 1 # 양방향 노드

    alst = []
    DFS(1)

    print(f'#{test_case}',*alst)




