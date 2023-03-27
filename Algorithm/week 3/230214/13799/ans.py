import sys
sys.stdin = open('s_input.txt', 'r')

def dfs_recur(s):
    for e in adj[s]:
        if v[e] == 0:
            v[e] = 1
            dfs_recur(e)


def dfs(s):
    stk = []

    while True:
        for e in adj[s] : # s에 연결된 노드를 순차적으로 확인한다
            if v[e] == 0 : # 미방문 시
                stk.append(s)
                s = e
                v[s] = 1
                break # 탈출하여 기준점부터 다시 동작한다
        else : # 연결된 게 하나도 없는 경우
            if stk != [] : s = stk.pop() # stack 이 안비어있으면 수행
            else : break # 비어있으면 error 이므로 루프 탈출

T = int(input())
for test_case in range(1,T+1):
    V,E = map(int,input().split()) # V: 노드의 개수 E : 간선의 개수
    adj=[[] for _ in range(V+1)] # 인접 리스트 만들기
    for _ in range(E) : # 노드들의 간선 정보
        s,e = map(int,input().split())
        adj[s].append(e)
    S,G = map(int,input().split()) # S: 출발 노드, G: 도착 노드

    v = [0]*(V+1) # visited list

    dfs(S) # 찾아도 끝까지 실행하는 동작
    # dfs_recur(S) # 재귀로 푸는 방법
    print(f'#{test_case} {v[G]}')