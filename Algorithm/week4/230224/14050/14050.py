import sys
sys.stdin = open('input.txt','r')

def BFS(S):
    # q, v 생성
    q = []
    v = [0]*101

    # initialize
    q.append(S)
    v[S] += 1

    # q 가 비어있지 않다면
    while q :
        c = q.pop(0)
        for e in adj[c] : # 연결된 노드
            if v[e] == 0 : # 미방문 노드
                q.append(e)
                v[e] = v[c] + 1
        else : pass # 이미 방문한 노드면 제외한다

    trials = 0 ; alst = []
    for i in range(101) :
        if v[i] != 0 and v[i] > trials : trials = v[i]
    for i in range(101):
        if v[i] == trials : alst.append(i)

    mx = 0
    for a in alst :
        if a > mx : mx = a
    return mx

T = 10
for test_case in range(1,T+1):
    N, start = map(int,input().split())
    lst = list(map(int,input().split()))
    adj = [[] for _ in range(101)]

    S,E = [],[]
    for i in range(len(lst)):
        if i % 2 : E.append(lst[i])
        else: S.append(lst[i])
    for x in range(len(S)):
        adj[S[x]].append(E[x])

    for lst in adj : lst.sort()

    print(f'#{test_case} {BFS(start)}')