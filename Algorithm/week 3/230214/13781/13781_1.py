import sys
sys.stdin = open('s_input.txt','r')

def DFS(S):
    v = [0] * (V+1)
    stk = []

    s = S
    v[s] = 1
    alst.append(s)

    while True :
        for e in adj[s]: # 연결된 노드
            if v[e] == 0 : # 미방문 노드
                stk.append(s)
                s = e
                v[s] = 1
                alst.append(s)
                break
        else : # 연결되지 않은 노드
            if stk : s = stk.pop() # 스택이 비어있지 않다면
            else : break


def QSORT(lst):
    # 종료 조건: 정렬할 요소가 한개일 때
    if len(lst) <= 1 : return lst

    # 단위 작업 : pivot 을 기준으로 좌/우 분리
    pivot = lst.pop()
    l,r = [],[]
    for n in lst :
        if n < pivot : l.append(n)
        else : r.append(n)
    return QSORT(l) + [pivot] + QSORT(r)

T = int(input())
for test_case in range(1,T+1):
    V, E = map(int,input().split()) # V : 노드의 수 E : 간선의 수

    # 1 연결 리스트에 연결된 노드들 표시
    adj = [[] for _ in range(V+1)]
    for _ in range(E):
        s,e = map(int,input().split())
        adj[s].append(e)
        adj[e].append(s)
    print(adj)

    # 2 필요한 틀 만들기
    alst = []
    DFS(1)
    print(f'#{test_case} {alst}')