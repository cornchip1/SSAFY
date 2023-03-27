import sys
sys.stdin = open('s_input.txt','r')

def BFS(S,G):
    # 1 q, v[] 생성
    q = []
    v = [0]*(V+1)

    # 2 q에 초기 데이터(들) 삽입, v[] 표시
    q.append(S)
    v[S] += 1

    # 3 q 가 비어있지 않을 때
    while q :
        c = q.pop(0) # q 의 첫번째 원소를 불러온다
        if c == G : return v[c]-1 # 간선의 수이므로 -1 을 뺀다
        # 반복
        for e in adj[c] :
            # 범위 내, 미방문, 조건 부합 시
            if v[e] == 0 :
                q.append(e)
                v[e] = v[c]+1

    # q를 다 돌았는데도 도착을 못한다면 0을 반환한다
    return 0

T = int(input())
for test_case in range(1,T+1):
    V,E = map(int,input().split())
    adj = [[] for _ in range(V+1)]

    # 간선 정보 받아오기
    for _ in range(E):
        s,e = map(int,input().split())
        adj[s].append(e)
        adj[e].append(s)

    # sort
    for lst in adj:
        lst.sort()

    # 출발, 도착 지점
    S,G = map(int,input().split())

    print(f'#{test_case} {BFS(S,G)}')