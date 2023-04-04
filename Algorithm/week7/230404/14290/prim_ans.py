import sys
sys.stdin = open('s_input.txt','r')

def Prim(ss):
    v[ss] = 1
    result = 0

    for _ in range(V): # 전체 노드 - 1 개만큼 반복 처리
        mn, mnidx = INF, 0
    # [1] MST에 포함된 노드를 하나씩 처리
        for s in range(V+1):
            if v[s] == 1 :
                # 포함 안 된 노드 중 최소비용 연결 노드 찾기
                for e in range(V+1):
                    if v[e] == 0 and mn > adj[s][e] :
                        mn, mnidx = adj[s][e], e
        v[mnidx] = 1
        result += mn

    return result

INF = 10 * 1000 + 1
T = int(input())
for tc in range(1,T+1):
    V,E = map(int,input().split())
    adj = [[INF]*(V+1) for _ in range(V+1)]

    for _ in range(E): # 양방향
        s,e,w = map(int,input().split())
        adj[s][e] = w
        adj[e][s] = w

    v = [0]*(V+1)
    ans = Prim(0)

    print(f'#{tc} {ans}')