V,E = map(int,input().split())
rep = [i for i in range(V+1)]
graph = []

def find_set(x):
    while x != rep[x] :
          x = rep[x]
    return x

def union(x,y):
    rep[find_set(y)] = find_set(x)

for _ in range(E):
    v1, v2, w = map(int,input().split())
    graph.append([v1,v2,w])

# 1 가중치 기준 오름차순 정렬
graph.sort(key = lambda x : x[2])

# 2 N개 정점 (V+1) , N-1 개의 간선 선택
N = V+1
s = 0 # MST에 포함된 간선의 가중치 합
cnt = 0
MST = []

for u,v,w in graph : # 가중치가 작은 것부터
    if find_set(u) != find_set(v) : # 사이클이 생기지 않으면
        cnt += 1
        s += 2
        MST.append([u,v,w])
        union(u,v)
        if cnt == N-1: # MST구성 완료
            break
print(s)


'''-----------------------------------------------------'''
def Dijkstra(s,V) : # 출발 정점, 마지막 정점 번호

    U = [0] * (V+1) # U : 최소 비용이 결정된 정점의 집합
    U[s] = 1

    for i in range(V+1) : # s 정점에서 나머지 정점 i로 가는 비용을 D에 기록
        D[i] = adjM[s][i]

    N = V+1 # N개의 정점
    for _ in range(N-1) : # N-1개 정점의 비용 결정
        # D[w] 가 최소인 w 결정
        minV = INF
        w = 0
        for i in range(V+1):
            if U[i] == 0 and minV > D[i] : # 비용이 확정되지 않은 정점 중 최소 비용을 가진 정점이면
                w = i
                minV = D[i]
        U[w] = 1 # 최소인 w는 최소비용 D[w] 확정
        # w에 인접인 정점에 대해, 기존비용과 w를 거쳐가는 비용 비교

        for v in range(V+1):
            if 0 < adjM[w][v] < INF : # w에 인접인 v의 조건
                D[v] = min(D[v],D[w]+adjM[w][v])

    return


INF= 100**2
V, E = map(int,input().split()) # 0~V번 정점, 간선 수
adjM = [[INF]*(V+1) for _ in range(V+1)]
for i in range(V+1):
    adjM[i][i] = 0 # 자기 자신으로 가는 비용

for _ in range(E):
    u,v,w = map(int,input().split()) # u -> v, w 가중치
    adjM[u][v] = w

D = [0]*(V+1)
Dijkstra(0,V)
print(D)





