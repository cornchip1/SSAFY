import sys
sys.stdin = open('s_input.txt','r')

def dfs(start):
    stk = []

    s = start
    v[s] = 1 # 시작 위치에서의 방문 표시

    while True:
        for e in adj[s] : # 인접리스트의 기준 위치에서 e 를 찾아서
            if v[e] == 0: # 방문하지 않은 경우
                stk.append(s) # 돌아오기 위해 기준점을 stk에 넣는다

                s = e # 기준점을 바꾸고
                v[s] = 1 # 방문 처리
                break # 루프 탈출
        else : # 연결된 점이 없으면
            if stk : # stk이 비어있지 않으면
                s = stk.pop() # 현 기준점에 더이상 탐색할 곳이 없는 경우 직전 기준점으로 되돌아간다
            else : break # stk 이 비어있으면 (즉, 갈 곳이 없으면) while 문 종료

T = 3 #10
for test_case in range(1,T+1):
    _tc, _N = map(int,input().split()) # _tc: 테스트 케이스의 번호, _N: 길의 총 개수
    lst = list(map(int,input().split()))
    N = 100
    adj = [[0] for _ in range(N)]

    for i in range(0,len(lst),2):
        s,e = lst[i],lst[i+1]
        adj[s].append(e)

    S,G = 0,99
    v = [0]*N

    dfs(S)

    print(f'#{test_case} {v[G]}')