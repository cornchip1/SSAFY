import sys
sys.stdin = open('s_input.txt','r')

def BFS(v,N) :
    # visited 배열 생성
    visited = [0] * (N+1)
    # queue 생성, 시작점 enqueue
    q = [v]
    # 시작점 enqueue 표시
    visited[v] = 1

    # queue 가 비어있지 않으면
    while q:
        t = q.pop(0) # dequeue
        alst.append(t) #print(t,end = ' ') # t에서 처리할 일 (무조건 dequeue 후 처리하라)
        # t에 인접이고 방문한 적 없는 v
        for v in adj[t] :
            if visited[v] == 0 :
                # v enqueue, enqueue 되었음 표시
                q.append(v)
                visited[v] = visited[t] + 1 # 몇번째 단계에서 방문했는지 기록이 됨
    return alst

T = int(input())
for test_case in range(1,T+1):
    V, E = map(int,input().split()) # V: 노드의 개수 E: 간선의 개수
    adj = [[] for _ in range(V+1)]
    for _ in range(E):
        s,e = map(int,input().split())
        adj[s].append(e)
        adj[e].append(s)
    alst = []
    print(f'#{test_case}', *BFS(1,V))
