import sys
sys.stdin = open('input.txt','r')

def Dijkstra(s,e):
    # [0] s에 해당하는 table 행 복사해오기
    D = adj[s][::]
    v = [0] * N # visited 배열 생성
    v[s] = 1 # 방문 처리

    # N-1개 노드에 대해 반복처리 반복
    for _ in range(N-1):
        # [1] 미방문 노드 중 최소비용 찾기
        mn, mnidx = INF, 0
        for j in range(N):
            if v[j] == 0 and mn > D[j] :
                mn, mnidx = D[j],j
        v[mnidx] = 1

        # [2] 모든 경로 update : 현재 비용, 찾은 노드의 비용 중 더 작은 값으로
        for j in range(N):
            D[j] = min(D[j],D[mnidx]+adj[mnidx][j])

    return D[e]

T = int(input())
for tc in range(1,T+1):
    N,E = map(int,input().split())
    INF = 10 * N + 1

    # 가중치 표 설정
    adj = [[INF]*N for _ in range(N)]
    # 나 자신으로 가는 경우 가중치는 0
    for i in range(N):
        adj[i][i] = 0
    for _ in range(E):
        s,e,w = map(int,input().split())
        adj[s][e] = w

    print(f'#{tc} {Dijkstra(0,N-1)}')