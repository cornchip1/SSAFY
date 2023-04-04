import sys
sys.stdin = open('input.txt','r')

def Dijkstra(s,e):
    # [0] D table, v[] 생성 및 시작위치 방문표시
    D = adj[s][::]
    v = [0]*N
    v[s] = 1

    # N-1개 노드에 대해서 반복처리
    for _ in range(N-1):
        # [1] 미방문 노드 중 기준 노드(최소 비용으로 연결 가능한 )
        mn, mnidx = INF,0
        for j in range(N):
            if v[j] == 0 and mn > D[j] :
                mn, mnidx = D[j],j
        v[mnidx] = 1 # 기준노드 방문 처리

        # [2] 모든 노드에 대해서 최소비용 갱신(D[])
        for j in range(N):
            # 현재 j 까지 가는 비용, 기준 노드를 경유해서 가는 비용
            D[j] = min(D[j],D[mnidx]+adj[mnidx][j])

    return D[e] # s -> e 까지의 최소비용용


INF= 50*10
T= int(input())
for tc in range(1,T+1):
    N, E = map(int,input().split())
    adj = [[INF]*N for _ in range(N)]

    # [0] 가중치 table 설정
    for i in range(N):
        adj[i][i] = 0 # 자기 자신으로 가는 비용은 0
    for _ in range(E):  # 간선 개수만큼 입력
        s,e,w = map(int,input().split())
        adj[s][e] = w

    ans = Dijkstra(0,N-1)
    print(f'#{tc} {ans}')