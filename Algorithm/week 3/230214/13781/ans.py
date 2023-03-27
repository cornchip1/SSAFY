import sys
sys.stdin = open('s_input.txt','r')

# 3 dfs 탐색
def dfs_stk(start):
    v = [0]*(V+1)
    stk = []

    # 3-1 첫 방문 표시, 경로 기록
    s = start
    v[s] = 1
    alst.append(s)

    # 3-2 stack 이 바닥날 때 까지 반복한다
    while True :
        # 3-2-1 s에서 연결된, 미방문의 노드 발견 시 이동 (단, 번호 오름차순)
        for e in range(1,V+1): # e: s와 연결되어있는 노드
            if v[e]==0 and adj[s][e]==1:
                stk.append(s) # 주의! 되돌아 올 위치를 push 하는 것 (즉, 지금의 기준점)
                s = e
                v[s] = 1
                alst.append(s)
                break # 찾았으면 즉시 그 곳을 기준으로 탐색해야 하므로 for 문 탈출
        # 3-2-2 더 이상 연결된 방문 노드가 없는 경우
        else:
            if stk : # stack 에 데이터가 있다면 (stack이 비어있지 않다면)
                s = stk.pop() # stack에서 꺼낸 최근 기준점이 현재 기준점이 된다
            else :
                break # stack 에 데이터가 없다면 탐색을 진행할 기준점이 없으니 종료

T = int(input())
for test_case in range(1,T+1):
    V,E = map(int,input().split())

    # 1 연결 array 에 연결된 노드들을 1로 표시
    adj = [[0]*(V+1) for _ in range(V+1)] # 인접한 list
    for _ in range(V):
        s,e = map(int,input().split())
        adj[s][e] = adj[e][s] = 1

    # 2 필요한 틀 만들기
    alst = [] # 경로를 넣는 list
    dfs_stk(1)

    print(f'#{test_case}',*alst)