import sys
sys.stdin = open('s_input.txt','r')

def dfs(si,sj) :
    stk = []

    ci,cj = si,sj # 기준 위치 저장
    v[ci][cj] = 1 # 초기 위치 방문 처리

    while True :
        # 4 방향 / 8 방향 / 연결된 링크 등등 범위 내 / 미방문 / '1' 이 아니면 탐색
        for di,dj in ((-1,0),(1,0),(0,-1),(0,1)):
            ni,nj = ci+di,cj+dj # 다음 좌표 찾기
            # 범위 안에 있다면 & 방문 안했으면 & 길이 있으면
            if 0 <= ni < N and 0 <= nj < N and v[ni][nj] == 0 and arr[ni][nj] != '1':
                stk.append((ci,cj))

                ci,cj = ni,nj
                v[ci][cj] = 1
                break # 기준점 찾으면 그 즉시 새로운 기준점으로 간다
        else : # 현재 기준점에서 더이상 탐색할 곳이 없다면
            if stk : ci,cj = stk.pop() # stack 이 있다면 stk 의 마지막 원소를 꺼낸다
            else : break

T = int(input())
for test_case in range(1,T+1):
    N = int(input())
    arr = [input() for _ in range(N)]
    v = [[0] * N for _ in range(N)]

    #si,sj,ei,ej = 0,0,0,0
    for i in range(N) :
        for j in range(N) :
            if arr[i][j] == '2':
                si,sj = i,j
            elif arr[i][j] == '3' :
                ei,ej = i,j

    dfs(si,sj)
    ans = v[ei][ej]

    print(f'#{test_case} {ans}')